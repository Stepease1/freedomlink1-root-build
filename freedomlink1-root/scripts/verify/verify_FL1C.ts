import { run } from "hardhat";
import addresses from "../utils/addresses.json";

async function main() {
  await run("verify:verify", {
    address: addresses.FL1C,
    constructorArguments: [
      addresses.GovernanceRouter,
      addresses.EpochManager,
      addresses.LineageRegistry,
      addresses.CreatorIdentityRegistry,
      addresses.RootstoneBinding
    ]
  });
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
