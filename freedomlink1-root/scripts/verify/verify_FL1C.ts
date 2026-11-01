import { run } from "hardhat";

async function main() {
  const variables = [
    "FL1C_ADDRESS",
    "FL1C_GOVERNANCE_ROUTER",
    "FL1C_EPOCH_AUTHORITY",
    "FL1C_ROOTSTONE_REGISTRY",
    "FL1C_LINEAGE_REGISTRY"
  ] as const;
  const values = variables.map((name) => process.env[name]);
  const missing = variables.filter((name) => !process.env[name]);
  if (missing.length > 0) throw new Error(`Missing verification settings: ${missing.join(", ")}`);

  await run("verify:verify", {
    address: values[0],
    constructorArguments: values.slice(1)
  });
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
