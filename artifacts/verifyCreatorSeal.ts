import * as fs from "fs";
import * as crypto from "crypto";

export interface CreatorSeal {
  creator_seal: {
    creator: string;
    institution: string;
    epoch: string;
    lineage: string;
    algorithm: {
      key_type: string;
      key_size: number;
      digest: string;
      encoding: string;
    };
    public_key: string;
    signature: string;
    manifest: {
      creator: string;
      institution: string;
      epoch: string;
      lineage: string;
      timestamp: string;
    };
  };
}

export function loadCreatorSeal(path: string): CreatorSeal {
  const raw = fs.readFileSync(path, "utf8");
  return JSON.parse(raw) as CreatorSeal;
}

export function buildManifestString(seal: CreatorSeal["creator_seal"]): string {
  return [
    `Creator: ${seal.manifest.creator}`,
    `Institution: ${seal.manifest.institution}`,
    `Epoch: ${seal.manifest.epoch}`,
    `Lineage: ${seal.manifest.lineage}`,
    `Timestamp: ${seal.manifest.timestamp}`
  ].join("\n");
}

export function verifyCreatorSeal(path: string): boolean {
  const seal = loadCreatorSeal(path).creator_seal;
  const manifestString = buildManifestString(seal);
  const signature = Buffer.from(seal.signature.replace(/\s+/g, ""), "base64");

  return crypto.verify(
    "sha256",
    Buffer.from(manifestString),
    {
      key: seal.public_key,
      padding: crypto.constants.RSA_PKCS1_PADDING
    },
    signature
  );
}

if (require.main === module) {
  const path = process.argv[2] || "creator-seal.json";
  const result = verifyCreatorSeal(path);
  console.log(`Creator Seal Verified: ${result}`);
}