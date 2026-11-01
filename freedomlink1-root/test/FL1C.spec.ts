import { expect } from "chai";
import { ethers } from "hardhat";

const Role = {
  NONE: 0,
  FOUNDER: 1,
  AGENCY: 2,
  TREASURY: 3,
  EDITORIAL: 4,
  ROOTSTONE: 5,
  GOVERNANCE: 6
} as const;

describe("FL1C Governance Credential", function () {
  async function deploy() {
    const [owner, userA, userB, stranger] = await ethers.getSigners();
    const governance: any = await (await ethers.getContractFactory("GovernanceRouter")).deploy(owner.address);
    const epochAuthority: any = await (await ethers.getContractFactory("EpochAuthority")).deploy(
      owner.address,
      7,
      ethers.keccak256(ethers.toUtf8Bytes("canonical-ledger-epoch7"))
    );
    const lineage: any = await (await ethers.getContractFactory("LineageRegistry")).deploy(owner.address);
    const rootstone: any = await (await ethers.getContractFactory("RootstoneRegistry")).deploy(owner.address);
    await epochAuthority.setLineageRegistry(await lineage.getAddress());
    await lineage.setEpochAuthority(await epochAuthority.getAddress());
    const lineageNode = ethers.keccak256(ethers.toUtf8Bytes("freedomlink1/epoch/7"));
    await epochAuthority.bindInitialLineage(lineageNode);
    await governance.setPermissions(owner.address, true, true, true);

    const fl1c: any = await (await ethers.getContractFactory("FL1C")).deploy(
      await governance.getAddress(),
      await epochAuthority.getAddress(),
      await rootstone.getAddress(),
      await lineage.getAddress()
    );
    await epochAuthority.registerEpochClient(await fl1c.getAddress());

    return { owner, governance, epochAuthority, userA, userB, stranger, rootstone, lineage, fl1c, lineageNode };
  }

  it("binds FL1C to the active epoch and registered lineage node", async function () {
    const { fl1c, lineage, lineageNode } = await deploy();

    expect(await fl1c.currentEpoch()).to.equal(7);
    expect(await fl1c.lineageNode()).to.equal(lineageNode);
    expect(await lineage.getLineageNode(7)).to.equal(lineageNode);
  });

  it("rejects unauthorized and unverified credential minting", async function () {
    const { owner, stranger, userA, userB, rootstone, fl1c } = await deploy();
    await rootstone.setAttestation(userA.address, ethers.keccak256(ethers.toUtf8Bytes("user-a-attestation")));

    await expect(
      fl1c.connect(stranger).mintCredential(userA.address, Role.FOUNDER, 100)
    ).to.be.revertedWith("FL1C: governance only");
    await expect(
      fl1c.connect(owner).mintCredential(userB.address, Role.FOUNDER, 100)
    ).to.be.revertedWith("FL1C: rootstone verification failed");
  });

  it("allows verified governance to mint a role-bound credential", async function () {
    const { owner, userA, rootstone, fl1c } = await deploy();
    await rootstone.setAttestation(userA.address, ethers.keccak256(ethers.toUtf8Bytes("user-a-attestation")));

    await expect(fl1c.connect(owner).mintCredential(userA.address, Role.FOUNDER, 100))
      .to.emit(fl1c, "CredentialMinted")
      .withArgs(userA.address, Role.FOUNDER, 100, 7);

    expect(await fl1c.balanceOf(userA.address)).to.equal(100);
    expect(await fl1c.roleOf(userA.address)).to.equal(Role.FOUNDER);
  });

  it("rejects a second role while the account has a balance", async function () {
    const { owner, userA, rootstone, fl1c } = await deploy();
    await rootstone.setAttestation(userA.address, ethers.keccak256(ethers.toUtf8Bytes("user-a-attestation")));
    await fl1c.connect(owner).mintCredential(userA.address, Role.FOUNDER, 100);

    await expect(
      fl1c.connect(owner).mintCredential(userA.address, Role.AGENCY, 1)
    ).to.be.revertedWith("FL1C: role mismatch");
  });

  it("allows governance to revoke a credential after Rootstone verification is lost", async function () {
    const { owner, userA, rootstone, fl1c } = await deploy();
    await rootstone.setAttestation(userA.address, ethers.keccak256(ethers.toUtf8Bytes("user-a-attestation")));
    await fl1c.connect(owner).mintCredential(userA.address, Role.FOUNDER, 100);
    await rootstone.revokeAttestation(userA.address);

    await expect(fl1c.connect(owner).burnCredential(userA.address, 100))
      .to.emit(fl1c, "CredentialBurned")
      .withArgs(userA.address, Role.FOUNDER, 100, 7);

    expect(await fl1c.balanceOf(userA.address)).to.equal(0);
    expect(await fl1c.roleOf(userA.address)).to.equal(Role.NONE);
  });

  it("restricts role changes to governance and Rootstone-verified accounts", async function () {
    const { owner, stranger, userA, rootstone, fl1c } = await deploy();
    await rootstone.setAttestation(userA.address, ethers.keccak256(ethers.toUtf8Bytes("user-a-attestation")));
    await fl1c.connect(owner).mintCredential(userA.address, Role.FOUNDER, 100);

    await expect(fl1c.connect(stranger).changeRole(userA.address, Role.AGENCY))
      .to.be.revertedWith("FL1C: governance only");
    await rootstone.revokeAttestation(userA.address);
    await expect(fl1c.connect(owner).changeRole(userA.address, Role.AGENCY))
      .to.be.revertedWith("FL1C: rootstone verification failed");
    await rootstone.setAttestation(userA.address, ethers.keccak256(ethers.toUtf8Bytes("user-a-attestation-2")));

    await expect(fl1c.connect(owner).changeRole(userA.address, Role.AGENCY))
      .to.emit(fl1c, "RoleChanged")
      .withArgs(userA.address, Role.FOUNDER, Role.AGENCY, 7);
    expect(await fl1c.roleOf(userA.address)).to.equal(Role.AGENCY);
  });

  it("seals, anchors, and advances the epoch atomically across registered clients", async function () {
    const { owner, epochAuthority, lineage, fl1c } = await deploy();
    const merkleRoot = ethers.keccak256(ethers.toUtf8Bytes("epoch7-root"));
    const nextNode = ethers.keccak256(ethers.toUtf8Bytes("epoch8"));
    const nextLedgerDigest = ethers.keccak256(ethers.toUtf8Bytes("epoch8-ledger"));

    await expect(epochAuthority.advanceEpoch(nextLedgerDigest, nextNode))
      .to.be.revertedWith("EpochAuthority: current epoch not sealed");
    await epochAuthority.connect(owner).sealCurrentEpoch(merkleRoot);
    expect(await lineage.getMerkleRoot(7)).to.equal(merkleRoot);

    await expect(epochAuthority.connect(owner).advanceEpoch(nextLedgerDigest, nextNode))
      .to.emit(epochAuthority, "EpochAdvanced")
      .withArgs(7, 8, nextNode, nextLedgerDigest);
    expect(await fl1c.currentEpoch()).to.equal(8);
    expect(await fl1c.lineageNode()).to.equal(nextNode);
    expect(await lineage.getLineageNode(8)).to.equal(nextNode);
  });

  it("disables transfer and approval methods", async function () {
    const { userA, userB, fl1c } = await deploy();

    await expect(fl1c.connect(userA).transfer(userB.address, 1))
      .to.be.revertedWith("FL1C: transfer disabled");
    await expect(fl1c.connect(userA).transferFrom(userA.address, userB.address, 1))
      .to.be.revertedWith("FL1C: transferFrom disabled");
    await expect(fl1c.connect(userA).approve(userB.address, 1))
      .to.be.revertedWith("FL1C: approve disabled");
    expect(await fl1c.allowance(userA.address, userB.address)).to.equal(0);
  });
});