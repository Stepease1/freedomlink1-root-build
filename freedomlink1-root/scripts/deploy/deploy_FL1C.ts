import { ethers } from "hardhat";
import addresses from "../utils/addresses.json";

async function main() {
  const FL1C = await ethers.getContractFactory("FL1C");

  const fl1c = await FL1C.deploy(
    addresses.GovernanceRouter,
    addresses.EpochManager,
    addresses.LineageRegistry,
    addresses.CreatorIdentityRegistry,
    addresses.RootstoneBinding
  );

  await fl1c.waitForDeployment();

  console.log("FL1C deployed at:", await fl1c.getAddress());
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
