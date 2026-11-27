import { expect } from "chai";
import { ethers } from "hardhat";
import SafeArtifact from "@safe-global/safe-contracts/build/artifacts/contracts/Safe.sol/Safe.json";
import SafeProxyFactoryArtifact from "@safe-global/safe-contracts/build/artifacts/contracts/proxies/SafeProxyFactory.sol/SafeProxyFactory.json";
import { Signer } from "ethers";

const Role = {
  FOUNDER: 1
} as const;

const ZERO_ADDRESS = ethers.ZeroAddress;

async function deploySafe(
  deployer: Signer,
  singleton: any,
  proxyFactory: any,
  owners: Signer[],
  threshold: number,
  saltNonce: number
) {
  const ownerAddresses = await Promise.all(owners.map((owner) => owner.getAddress()));
  const initializer = singleton.interface.encodeFunctionData("setup", [
    ownerAddresses,
    threshold,
    ZERO_ADDRESS,
    "0x",
    ZERO_ADDRESS,
    ZERO_ADDRESS,
    0,
    ZERO_ADDRESS
  ]);
  const proxyAddress = await proxyFactory.createProxyWithNonce.staticCall(
    await singleton.getAddress(),
    initializer,
    saltNonce
  );
  await (await proxyFactory.createProxyWithNonce(
    await singleton.getAddress(),
    initializer,
    saltNonce
  )).wait();

  return new ethers.Contract(proxyAddress, SafeArtifact.abi, deployer);
}

async function buildSafeSignatures(
  safe: any,
  owners: Signer[],
  to: string,
  data: string,
  signers: Signer[]
) {
  const nonce = await safe.nonce();
  const safeTxHash = await safe.getTransactionHash(
    to,
    0,
    data,
    0,
    0,
    0,
    0,
    ZERO_ADDRESS,
    ZERO_ADDRESS,
    nonce
  );
  const ownerAddresses = await Promise.all(owners.map((owner) => owner.getAddress()));
  const signatureEntries = await Promise.all(signers.map(async (signer) => {
    const signerAddress = await signer.getAddress();
    expect(ownerAddresses.map((address) => address.toLowerCase())).to.include(
      signerAddress.toLowerCase()
    );

    const signature = ethers.Signature.from(
      await signer.signMessage(ethers.getBytes(safeTxHash))
    );
    const safeV = signature.v + 4;

    return {
      signerAddress,
      signature: ethers.concat([
        signature.r,
        signature.s,
        ethers.toBeHex(safeV, 1)
      ])
    };
  }));
  signatureEntries.sort((left, right) =>
    left.signerAddress.toLowerCase().localeCompare(right.signerAddress.toLowerCase())
  );

  return ethers.concat(signatureEntries.map((entry) => entry.signature));
}

async function executeSafeTransaction(
  safe: any,
  owners: Signer[],
  executor: Signer,
  to: string,
  data: string,
  signers: Signer[]
) {
  const signatures = await buildSafeSignatures(safe, owners, to, data, signers);
  return safe.connect(executor).getFunction("execTransaction")(
    to,
    0,
    data,
    0,
    0,
    0,
    0,
    ZERO_ADDRESS,
    ZERO_ADDRESS,
    signatures
  );
}

describe("GovernanceRouter with deployed Safe wallets", function () {
  async function deploy() {
    const [
      ownerA,
      ownerB,
      ownerC,
      recipient,
      stranger,
      nextOwnerA,
      nextOwnerB,
      nextOwnerC
    ] = await ethers.getSigners();
    const [safeImplementation, safeProxyFactory] = await Promise.all([
      new ethers.ContractFactory(SafeArtifact.abi, SafeArtifact.bytecode, ownerA).deploy(),
      new ethers.ContractFactory(
        SafeProxyFactoryArtifact.abi,
        SafeProxyFactoryArtifact.bytecode,
        ownerA
      ).deploy()
    ]);
    await Promise.all([
      safeImplementation.waitForDeployment(),
      safeProxyFactory.waitForDeployment()
    ]);

    const safeOwners = [ownerA, ownerB, ownerC];
    const safe = await deploySafe(
      ownerA,
      safeImplementation,
      safeProxyFactory,
      safeOwners,
      2,
      1
    );
    const safeAddress = await safe.getAddress();

    const epochAuthority: any = await (
      await ethers.getContractFactory("EpochAuthority")
    ).deploy(
      ownerA.address,
      7,
      ethers.keccak256(ethers.toUtf8Bytes("safe-wallet-ledger-7"))
    );
    const lineage: any = await (
      await ethers.getContractFactory("LineageRegistry")
    ).deploy(ownerA.address);
    const rootstone: any = await (
      await ethers.getContractFactory("RootstoneRegistry")
    ).deploy(ownerA.address);

    await epochAuthority.setLineageRegistry(await lineage.getAddress());
    await lineage.setEpochAuthority(await epochAuthority.getAddress());
    const initialNode = ethers.keccak256(ethers.toUtf8Bytes("safe-wallet-lineage-7"));
    await epochAuthority.bindInitialLineage(initialNode);
    await rootstone.setAttestation(
      recipient.address,
      ethers.keccak256(ethers.toUtf8Bytes("safe-wallet-recipient"))
    );

    const routerNonce = await ownerA.getNonce();
    const predictedFL1C = ethers.getCreateAddress({
      from: ownerA.address,
      nonce: routerNonce + 1
    });
    const router: any = await (
      await ethers.getContractFactory("GovernanceRouter")
    ).deploy(
      safeAddress,
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
      ownerA,
      ownerB,
      ownerC,
      recipient,
      stranger,
      nextOwnerA,
      nextOwnerB,
      nextOwnerC,
      safeOwners,
      safe,
      safeAddress,
      safeImplementation,
      safeProxyFactory,
      router,
      epochAuthority,
      lineage,
      rootstone,
      fl1c,
      initialNode
    };
  }

  it("uses a 2-of-3 Safe as router authority and gates credential issuance and revocation", async function () {
    const {
      ownerA,
      ownerB,
      ownerC,
      recipient,
      stranger,
      safeOwners,
      safe,
      safeAddress,
      router,
      fl1c
    } = await deploy();
    const setPermissionsData = router.interface.encodeFunctionData("setPermissions", [
      safeAddress,
      true,
      true,
      true
    ]);

    expect(await router.governanceAuthority()).to.equal(safeAddress);
    expect(await safe.getThreshold()).to.equal(2);
    expect(Array.from(await safe.getOwners())).to.have.members(
      await Promise.all(safeOwners.map((owner) => owner.getAddress()))
    );

    const oneSignature = await buildSafeSignatures(
      safe,
      safeOwners,
      await router.getAddress(),
      setPermissionsData,
      [ownerA]
    );
    await expect(
      safe.connect(ownerA).getFunction("execTransaction")(
        await router.getAddress(),
        0,
        setPermissionsData,
        0,
        0,
        0,
        0,
        ZERO_ADDRESS,
        ZERO_ADDRESS,
        oneSignature
      )
    ).to.be.revertedWith("GS020");

    await expect(
      executeSafeTransaction(
        safe,
        safeOwners,
        ownerA,
        await router.getAddress(),
        setPermissionsData,
        [ownerA, ownerB]
      )
    ).to.emit(router, "PermissionsUpdated").withArgs(safeAddress, true, true, true);

    await expect(
      router.connect(ownerA).setPermissions(ownerA.address, true, true, true)
    ).to.be.revertedWith("GovernanceRouter: owner only");
    await expect(
      fl1c.connect(stranger).mintCredential(recipient.address, Role.FOUNDER, 25)
    ).to.be.revertedWith("FL1C: governance only");
    await expect(
      fl1c.connect(ownerC).burnCredential(recipient.address, 1)
    ).to.be.revertedWith("FL1C: governance only");

    await expect(
      executeSafeTransaction(
        safe,
        safeOwners,
        ownerC,
        await fl1c.getAddress(),
        fl1c.interface.encodeFunctionData("mintCredential", [
          recipient.address,
          Role.FOUNDER,
          25
        ]),
        [ownerA, ownerC]
      )
    ).to.emit(fl1c, "CredentialMinted").withArgs(recipient.address, Role.FOUNDER, 25, 7);
    expect(await fl1c.balanceOf(recipient.address)).to.equal(25);

    await expect(
      executeSafeTransaction(
        safe,
        safeOwners,
        ownerB,
        await fl1c.getAddress(),
        fl1c.interface.encodeFunctionData("burnCredential", [recipient.address, 25]),
        [ownerB, ownerC]
      )
    ).to.emit(fl1c, "CredentialBurned").withArgs(recipient.address, Role.FOUNDER, 25, 7);
    expect(await fl1c.balanceOf(recipient.address)).to.equal(0);
  });

  it("advances epochs through Safe and preserves lineage and client synchronization", async function () {
    const {
      ownerA,
      ownerB,
      stranger,
      safeOwners,
      safe,
      safeAddress,
      epochAuthority,
      lineage,
      fl1c,
      initialNode
    } = await deploy();
    const merkleRoot = ethers.keccak256(ethers.toUtf8Bytes("safe-wallet-merkle-7"));
    const nextDigest = ethers.keccak256(ethers.toUtf8Bytes("safe-wallet-ledger-8"));
    const nextNode = ethers.keccak256(ethers.toUtf8Bytes("safe-wallet-lineage-8"));

    await epochAuthority.transferOwnership(safeAddress);
    expect(await epochAuthority.owner()).to.equal(safeAddress);
    expect(await lineage.getLineageNode(7)).to.equal(initialNode);

    await expect(
      epochAuthority.connect(ownerA).advanceEpoch(nextDigest, nextNode)
    ).to.be.revertedWith("EpochAuthority: owner only");

    await executeSafeTransaction(
      safe,
      safeOwners,
      ownerA,
      await epochAuthority.getAddress(),
      epochAuthority.interface.encodeFunctionData("sealCurrentEpoch", [merkleRoot]),
      [ownerA, ownerB]
    );
    expect(await lineage.getMerkleRoot(7)).to.equal(merkleRoot);

    await executeSafeTransaction(
      safe,
      safeOwners,
      ownerB,
      await epochAuthority.getAddress(),
      epochAuthority.interface.encodeFunctionData("advanceEpoch", [nextDigest, nextNode]),
      [ownerA, ownerB]
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

  it("transfers router authority from one Safe to another with both thresholds", async function () {
    const {
      ownerA,
      ownerB,
      ownerC,
      nextOwnerA,
      nextOwnerB,
      nextOwnerC,
      safeOwners,
      safe,
      safeImplementation,
      safeProxyFactory,
      router
    } = await deploy();
    const nextSafeOwners = [nextOwnerA, nextOwnerB, nextOwnerC];
    const nextSafe = await deploySafe(
      ownerA,
      safeImplementation,
      safeProxyFactory,
      nextSafeOwners,
      2,
      2
    );
    const nextSafeAddress = await nextSafe.getAddress();
    const proposalData = router.interface.encodeFunctionData("proposeGovernanceAuthority", [
      nextSafeAddress
    ]);
    const acceptanceData = router.interface.encodeFunctionData("acceptGovernanceAuthority");

    await expect(
      router.connect(ownerA).proposeGovernanceAuthority(nextSafeAddress)
    ).to.be.revertedWith("GovernanceRouter: owner only");

    await expect(
      executeSafeTransaction(
        safe,
        safeOwners,
        ownerA,
        await router.getAddress(),
        proposalData,
        [ownerA, ownerC]
      )
    ).to.emit(router, "GovernanceAuthorityTransferProposed")
      .withArgs(await safe.getAddress(), nextSafeAddress);
    expect(await router.governanceAuthority()).to.equal(await safe.getAddress());
    expect(await router.pendingGovernanceAuthority()).to.equal(nextSafeAddress);

    await executeSafeTransaction(
      nextSafe,
      nextSafeOwners,
      nextOwnerC,
      await router.getAddress(),
      acceptanceData,
      [nextOwnerA, nextOwnerB]
    );

    expect(await router.governanceAuthority()).to.equal(nextSafeAddress);
    expect(await router.pendingGovernanceAuthority()).to.equal(ZERO_ADDRESS);
  });
});
