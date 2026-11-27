import { expect } from "chai";
import { ethers } from "hardhat";

describe("GovernanceRouter hardening", function () {
  async function deploy() {
    const [authority, pendingAuthority, stranger, userA, userB] = await ethers.getSigners();
    const epochAuthority: any = await (await ethers.getContractFactory("EpochAuthority")).deploy(
      authority.address,
      7,
      ethers.keccak256(ethers.toUtf8Bytes("governance-router-ledger"))
    );
    const lineage: any = await (await ethers.getContractFactory("LineageRegistry")).deploy(authority.address);

    const routerNonce = await authority.getNonce();
    const predictedFl1cAddress = ethers.getCreateAddress({
      from: authority.address,
      nonce: routerNonce + 1
    });
    const router: any = await (await ethers.getContractFactory("GovernanceRouter")).deploy(
      authority.address,
      predictedFl1cAddress,
      await epochAuthority.getAddress(),
      await lineage.getAddress()
    );

    return {
      authority,
      pendingAuthority,
      stranger,
      userA,
      userB,
      router,
      predictedFl1cAddress,
      epochAuthority,
      lineage
    };
  }

  it("validates constructor dependencies", async function () {
    const factory = await ethers.getContractFactory("GovernanceRouter");
    const [authority, fl1c, epochManager, lineageRegistry] = await ethers.getSigners();
    const validArgs = [authority.address, fl1c.address, epochManager.address, lineageRegistry.address];
    const expectedErrors = [
      "GovernanceRouter: zero authority",
      "GovernanceRouter: zero FL1C",
      "GovernanceRouter: zero epoch manager",
      "GovernanceRouter: zero lineage registry"
    ];

    for (let i = 0; i < validArgs.length; i++) {
      const invalidArgs = [...validArgs];
      invalidArgs[i] = ethers.ZeroAddress;
      await expect(factory.deploy(...invalidArgs)).to.be.revertedWith(expectedErrors[i]);
    }
  });

  it("requires a two-step authority transfer", async function () {
    const { authority, pendingAuthority, stranger, router } = await deploy();

    await expect(router.connect(stranger).proposeGovernanceAuthority(pendingAuthority.address))
      .to.be.revertedWith("GovernanceRouter: owner only");

    await expect(router.connect(authority).proposeGovernanceAuthority(pendingAuthority.address))
      .to.emit(router, "GovernanceAuthorityTransferProposed")
      .withArgs(authority.address, pendingAuthority.address);

    expect(await router.pendingGovernanceAuthority()).to.equal(pendingAuthority.address);

    await expect(router.connect(stranger).acceptGovernanceAuthority())
      .to.be.revertedWith("GovernanceRouter: pending authority only");

    await expect(router.connect(pendingAuthority).acceptGovernanceAuthority())
      .to.emit(router, "GovernanceAuthorityTransferAccepted")
      .withArgs(authority.address, pendingAuthority.address);

    expect(await router.governanceAuthority()).to.equal(pendingAuthority.address);
    expect(await router.owner()).to.equal(pendingAuthority.address);
  });

  it("allows the current authority to cancel a pending transfer", async function () {
    const { authority, pendingAuthority, router } = await deploy();

    await router.connect(authority).proposeGovernanceAuthority(pendingAuthority.address);
    await expect(router.connect(authority).cancelGovernanceAuthorityTransfer())
      .to.emit(router, "GovernanceAuthorityTransferCancelled")
      .withArgs(pendingAuthority.address);

    expect(await router.pendingGovernanceAuthority()).to.equal(ethers.ZeroAddress);
  });

  it("keeps the legacy ownership entry point two-step", async function () {
    const { authority, pendingAuthority, router } = await deploy();

    await expect(router.connect(authority).transferOwnership(pendingAuthority.address))
      .to.emit(router, "GovernanceAuthorityTransferProposed")
      .withArgs(authority.address, pendingAuthority.address);
    expect(await router.governanceAuthority()).to.equal(authority.address);

    await router.connect(pendingAuthority).acceptGovernanceAuthority();
    expect(await router.governanceAuthority()).to.equal(pendingAuthority.address);
  });

  it("limits batch permission updates", async function () {
    const { authority, userA, userB, router } = await deploy();
    await router.connect(authority).setPermissions(userA.address, true, true, true);

    expect(await router.canMint(userA.address)).to.equal(true);
    expect(await router.canBurn(userA.address)).to.equal(true);
    expect(await router.canChangeRole(userA.address)).to.equal(true);

    await router.connect(authority).batchSetPermissions(
      [userA.address, userB.address],
      [false, true],
      [true, false],
      [true, false]
    );

    expect(await router.canMint(userA.address)).to.equal(false);
    expect(await router.canBurn(userA.address)).to.equal(true);
    expect(await router.canChangeRole(userA.address)).to.equal(true);

    const accounts = Array.from({ length: 101 }, () => userA.address);
    await expect(
      router.connect(authority).batchSetPermissions(
        accounts,
        accounts.map(() => true),
        accounts.map(() => true),
        accounts.map(() => true)
      )
    ).to.be.revertedWith("GovernanceRouter: batch limit exceeded");
  });

  it("exposes validated dependency addresses", async function () {
    const { router, predictedFl1cAddress, epochAuthority, lineage } = await deploy();

    expect(await router.fl1c()).to.equal(predictedFl1cAddress);
    expect(await router.epochManager()).to.equal(await epochAuthority.getAddress());
    expect(await router.lineageRegistry()).to.equal(await lineage.getAddress());
  });
});
