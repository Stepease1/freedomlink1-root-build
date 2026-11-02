import { createHash } from "node:crypto";
import { readFileSync, writeFileSync } from "node:fs";
import { isAbsolute, relative, resolve, sep } from "node:path";

type TreeConfig = {
  id: string;
  name: string;
  artifacts: string[];
};

type Manifest = {
  epoch: number;
  lineageNode: string;
  trees: TreeConfig[];
};

function isRecord(value: unknown): value is Record<string, unknown> {
  return typeof value === "object" && value !== null && !Array.isArray(value);
}

function parseManifest(value: unknown): Manifest {
  if (
    !isRecord(value) ||
    typeof value.epoch !== "number" ||
    !Number.isInteger(value.epoch) ||
    typeof value.lineageNode !== "string" ||
    value.lineageNode.length === 0 ||
    !Array.isArray(value.trees)
  ) {
    throw new Error("Invalid Merkle forest manifest: expected epoch, lineageNode, and trees.");
  }

  const treeIds = new Set<string>();
  const trees = value.trees.map((tree, index): TreeConfig => {
    if (
      !isRecord(tree) ||
      typeof tree.id !== "string" ||
      tree.id.length === 0 ||
      typeof tree.name !== "string" ||
      !Array.isArray(tree.artifacts) ||
      tree.artifacts.length === 0 ||
      !tree.artifacts.every((artifact) => typeof artifact === "string" && artifact.length > 0)
    ) {
      throw new Error(`Invalid Merkle forest manifest: tree at index ${index} is malformed.`);
    }
    if (treeIds.has(tree.id)) {
      throw new Error(`Invalid Merkle forest manifest: duplicate tree id "${tree.id}".`);
    }
    treeIds.add(tree.id);

    return {
      id: tree.id,
      name: tree.name,
      artifacts: tree.artifacts
    };
  });

  return {
    epoch: value.epoch,
    lineageNode: value.lineageNode,
    trees
  };
}

function sha256Hex(data: Buffer | string): string {
  return createHash("sha256").update(data).digest("hex");
}

function escapeXml(text: string): string {
  return text.replace(/[<>&"']/g, (character) => {
    const entities: Record<string, string> = {
      "<": "&lt;",
      ">": "&gt;",
      "&": "&amp;",
      '"': "&quot;",
      "'": "&apos;"
    };
    return entities[character];
  });
}

function replaceText(svg: string, id: string, text: string): string {
  const pattern = new RegExp(`(<text\\b[^>]*\\bid="${id}"[^>]*>)([\\s\\S]*?)(</text>)`, "g");
  const matches = [...svg.matchAll(pattern)];
  if (matches.length !== 1) {
    throw new Error(`Expected exactly one SVG text element with id "${id}", found ${matches.length}.`);
  }
  return svg.replace(pattern, (_match, openingTag: string, _content: string, closingTag: string) =>
    `${openingTag}${escapeXml(text)}${closingTag}`
  );
}

function main(): void {
  const projectRoot = process.cwd();
  const docsRoot = resolve(projectRoot, "..", "docs");
  const manifestPath = resolve(docsRoot, "merkle-forest.json");
  const svgPath = resolve(docsRoot, "merkle-forest.svg");
  const hashesPath = resolve(docsRoot, "merkle-forest-hashes.json");
  const manifest = parseManifest(JSON.parse(readFileSync(manifestPath, "utf8")));

  const leafHashes: { id: string; artifact: string; hash: string }[] = [];
  const treeHashes: { id: string; hash: string }[] = [];

  for (const tree of manifest.trees) {
    const leafHashesForTree: string[] = [];

    for (const artifact of tree.artifacts) {
      const artifactPath = resolve(projectRoot, artifact);
      const relativeArtifactPath = relative(projectRoot, artifactPath);
      if (
        isAbsolute(artifact) ||
        relativeArtifactPath === ".." ||
        relativeArtifactPath.startsWith(`..${sep}`) ||
        isAbsolute(relativeArtifactPath)
      ) {
        throw new Error(`Artifact path must stay inside the project: "${artifact}".`);
      }

      const hash = sha256Hex(readFileSync(artifactPath));
      leafHashes.push({ id: tree.id, artifact, hash });
      leafHashesForTree.push(hash);
    }

    treeHashes.push({ id: tree.id, hash: sha256Hex(leafHashesForTree.join("")) });
  }

  const forestRoot = sha256Hex(treeHashes.map((tree) => tree.hash).join(""));
  const hashesJson = {
    epoch: manifest.epoch,
    lineageNode: manifest.lineageNode,
    forestRoot,
    trees: treeHashes,
    leaves: leafHashes
  };

  let svg = readFileSync(svgPath, "utf8");
  for (const tree of manifest.trees) {
    const leafHash = leafHashes.find((leaf) => leaf.id === tree.id)?.hash;
    const treeHash = treeHashes.find((entry) => entry.id === tree.id)?.hash;
    if (!leafHash || !treeHash) {
      throw new Error(`Unable to resolve hashes for tree "${tree.id}".`);
    }
    svg = replaceText(svg, `leaf-${tree.id}-hash`, `Hash: ${leafHash}`);
    svg = replaceText(svg, `tree-${tree.id}-hash`, `Tree Hash: ${treeHash}`);
  }
  svg = replaceText(svg, "forest-root-hash", `Forest Root Hash: ${forestRoot}`);
  svg = replaceText(svg, "forest-epoch", `Epoch: ${manifest.epoch}`);
  svg = replaceText(svg, "forest-lineage", `Lineage Node: ${manifest.lineageNode}`);

  writeFileSync(hashesPath, `${JSON.stringify(hashesJson, null, 2)}\n`);
  writeFileSync(svgPath, svg);
}

main();
