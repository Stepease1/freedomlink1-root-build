import { expect } from "chai";
import { ethers } from "hardhat";

const Role = {
  FOUNDER: 1
} as const;

describe("GovernanceRouter with Safe-like authority", function () {
  async function deploy() {
    const [founder, recipient, stranger, newAuthority] = await ethers.getSigners();
    const safe: any = await (await ethers.getContractFactory("MockSafe")).deploy(founder.address);
    const epochAuthority: any = await (await ethers.getContractFactory("EpochAuthority")).deploy(
      founder.address,
      7,
      ethers.keccak256(ethers.toUtf8Bytes("safe-governance-ledger-7"))
    );
    const lineage: any = await (await ethers.getContractFactory("LineageRegistry")).deploy(founder.address);
    const rootstone: any = await (await ethers.getContractFactory("RootstoneRegistry")).deploy(founder.address);

    await epochAuthority.setLineageRegistry(await lineage.getAddress());
    await lineage.setEpochAuthority(await epochAuthority.getAddress());
    const initialNode = ethers.keccak256(ethers.toUtf8Bytes("safe-governance-lineage-7"));
    await epochAuthority.bindInitialLineage(initialNode);
    await rootstone.setAttestation(
      recipient.address,
      ethers.keccak256(ethers.toUtf8Bytes("safe-governance-recipient"))
    );

    const routerNonce = await founder.getNonce();
    const predictedFL1C = ethers.getCreateAddress({
      from: founder.address,
      nonce: routerNonce + 1
    });
    const router: any = await (await ethers.getContractFactory("GovernanceRouter")).deploy(
      await safe.getAddress(),
      predictedFL1C,
      await epochAuthority.getAddress(),
      await lineage.getAddress()
    );
    const fl1c: any = await (await ethers.getContractFactory("FL1C")).deploy(
      await router.getAddress(),
      await epochAuthority.getAddress(),
      await rootstone.getAddress(),
      await lineage.getAddress()
    );

    expect(await fl1c.getAddress()).to.equal(predictedFL1C);
    expect(await router.fl1c()).to.equal(await fl1c.getAddress());
    await epochAuthority.registerEpochClient(await fl1c.getAddress());

    return {
      founder,
      recipient,
      stranger,
      newAuthority,
      safe,
      router,
      epochAuthority,
      lineage,
      rootstone,
      fl1c,
      initialNode
    };
  }

  it("allows Safe-mediated FL1C credential issuance and revocation", async function () {
    const { founder, recipient, safe, router, fl1c } = await deploy();
    const safeAddress = await safe.getAddress();

    await safe.execute(
      await router.getAddress(),
      router.interface.encodeFunctionData("setPermissions", [safeAddress, true, true, true])
    );

    await expect(
      fl1c.connect(founder).mintCredential(recipient.address, Role.FOUNDER, 10)
    ).to.be.revertedWith("FL1C: governance only");

    await safe.execute(
      await fl1c.getAddress(),
      fl1c.interface.encodeFunctionData("mintCredential", [recipient.address, Role.FOUNDER, 10])
    );
    expect(await fl1c.balanceOf(recipient.address)).to.equal(10);

    await safe.execute(
      await fl1c.getAddress(),
      fl1c.interface.encodeFunctionData("burnCredential", [recipient.address, 10])
    );
    expect(await fl1c.balanceOf(recipient.address)).to.equal(0);
  });

  it("allows Safe-mediated epoch advancement and lineage synchronization", async function () {
    const { founder, stranger, safe, epochAuthority, lineage, fl1c, initialNode } = await deploy();
    const safeAddress = await safe.getAddress();
    const merkleRoot = ethers.keccak256(ethers.toUtf8Bytes("safe-governance-merkle-7"));
    const nextDigest = ethers.keccak256(ethers.toUtf8Bytes("safe-governance-ledger-8"));
    const nextNode = ethers.keccak256(ethers.toUtf8Bytes("safe-governance-lineage-8"));

    await epochAuthority.transferOwnership(safeAddress);
    expect(await epochAuthority.owner()).to.equal(safeAddress);
    expect(await lineage.getLineageNode(7)).to.equal(initialNode);

    await expect(
      epochAuthority.connect(founder).sealCurrentEpoch(merkleRoot)
    ).to.be.revertedWith("EpochAuthority: owner only");

    await safe.execute(
      await epochAuthority.getAddress(),
      epochAuthority.interface.encodeFunctionData("sealCurrentEpoch", [merkleRoot])
    );
    await safe.execute(
      await epochAuthority.getAddress(),
      epochAuthority.interface.encodeFunctionData("advanceEpoch", [nextDigest, nextNode])
    );

    expect(await epochAuthority.currentEpoch()).to.equal(8);
    expect(await lineage.getLineageNode(8)).to.equal(nextNode);
    expect(await fl1c.currentEpoch()).to.equal(8);
    expect(await fl1c.lineageNode()).to.equal(nextNode);
    await expect(
      epochAuthority.connect(stranger).advanceEpoch(
        ethers.keccak256(ethers.toUtf8Bytes("unauthorized")),
        ethers.keccak256(ethers.toUtf8Bytes("unauthorized-node"))
      )
    ).to.be.revertedWith("EpochAuthority: owner only");
  });

  it("supports Safe-mediated two-step authority transfer and rejects direct EOA control", async function () {
    const { founder, newAuthority, safe, router } = await deploy();
    const newAuthorityAddress = newAuthority.address;

    await expect(
      router.connect(founder).proposeGovernanceAuthority(newAuthorityAddress)
    ).to.be.revertedWith("GovernanceRouter: owner only");

    await safe.execute(
      await router.getAddress(),
      router.interface.encodeFunctionData("proposeGovernanceAuthority", [newAuthorityAddress])
    );
    expect(await router.governanceAuthority()).to.equal(await safe.getAddress());
    expect(await router.pendingGovernanceAuthority()).to.equal(newAuthorityAddress);

    await router.connect(newAuthority).acceptGovernanceAuthority();
    expect(await router.governanceAuthority()).to.equal(newAuthorityAddress);
    expect(await router.pendingGovernanceAuthority()).to.equal(ethers.ZeroAddress);
  });

  it("rejects execution requests from a non-owner of the Safe-like contract", async function () {
    const { stranger, safe, router } = await deploy();

    await expect(
      safe.connect(stranger).execute(
        await router.getAddress(),
        router.interface.encodeFunctionData("setPermissions", [stranger.address, true, true, true])
      )
    ).to.be.revertedWith("MockSafe: owner only");
  });
});
