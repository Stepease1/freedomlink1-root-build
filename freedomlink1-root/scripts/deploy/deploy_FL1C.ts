import { ethers, network } from "hardhat";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
import addresses from "../utils/addresses.json";

async function main() {
  if (network.name !== "localhost" && network.name !== "hardhat") {
    throw new Error("This scaffold deploys local governance instances only; use a reviewed production deployment process");
  }

  const [deployer] = await ethers.getSigners();
  if (!deployer) throw new Error("No local deployer signer is available");

  const ledgerPath = resolve(__dirname, "../../../lineage/epoch-ledger.md");
  const ledgerDigest = ethers.keccak256(readFileSync(ledgerPath));
  const lineageNode = ethers.keccak256(ethers.toUtf8Bytes(addresses.lineageIdentity));

  const GovernanceRouter = await ethers.getContractFactory("GovernanceRouter");
  const governanceRouter = await GovernanceRouter.deploy(deployer.address);
  await governanceRouter.waitForDeployment();
  await governanceRouter.setPermissions(deployer.address, true, true, true);

  const EpochAuthority = await ethers.getContractFactory("EpochAuthority");
  const epochAuthority = await EpochAuthority.deploy(deployer.address, addresses.currentEpoch, ledgerDigest);
  await epochAuthority.waitForDeployment();

  const LineageRegistry = await ethers.getContractFactory("LineageRegistry");
  const lineageRegistry = await LineageRegistry.deploy(deployer.address);
  await lineageRegistry.waitForDeployment();
  await epochAuthority.setLineageRegistry(await lineageRegistry.getAddress());
  await lineageRegistry.setEpochAuthority(await epochAuthority.getAddress());
  await epochAuthority.bindInitialLineage(lineageNode);

  const RootstoneRegistry = await ethers.getContractFactory("RootstoneRegistry");
  const rootstoneRegistry = await RootstoneRegistry.deploy(deployer.address);
  await rootstoneRegistry.waitForDeployment();
  const localAttestation = ethers.keccak256(
    ethers.toUtf8Bytes(`local-development-attestation:${deployer.address.toLowerCase()}`)
  );
  await rootstoneRegistry.setAttestation(deployer.address, localAttestation);

  const FL1C = await ethers.getContractFactory("FL1C");
  const fl1c = await FL1C.deploy(
    await governanceRouter.getAddress(),
    await epochAuthority.getAddress(),
    await rootstoneRegistry.getAddress(),
    await lineageRegistry.getAddress()
  );
  await fl1c.waitForDeployment();
  await epochAuthority.registerEpochClient(await fl1c.getAddress());

  console.log("Local governance router:", await governanceRouter.getAddress());
  console.log("Local epoch authority:", await epochAuthority.getAddress());
  console.log("Local Rootstone registry:", await rootstoneRegistry.getAddress());
  console.log("Local lineage registry:", await lineageRegistry.getAddress());
  console.log("FL1C deployed at:", await fl1c.getAddress());
  console.log("Epoch:", addresses.currentEpoch);
  console.log("Lineage node:", lineageNode);
  console.log("Canonical ledger digest:", ledgerDigest);
  console.log("Rootstone attestation is a local test fixture, not hardware attestation.");
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
