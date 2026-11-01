// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "../interfaces/IEpochAuthority.sol";
import "../interfaces/IEpochClient.sol";
import "../interfaces/ILineageRegistry.sol";

contract EpochAuthority is IEpochAuthority {
    uint256 public constant MAX_EPOCH_CLIENTS = 32;

    address public owner;
    uint256 public override currentEpoch;
    bytes32 public currentLedgerDigest;
    ILineageRegistry public lineageRegistry;

    mapping(uint256 => bool) public isEpochSealed;
    mapping(uint256 => bytes32) public ledgerDigestOf;
    mapping(address => bool) public isEpochClient;
    address[] private _epochClients;

    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);
    event LineageRegistrySet(address indexed lineageRegistry);
    event EpochClientRegistered(address indexed client);
    event InitialLineageBound(uint256 indexed epochId, bytes32 indexed node);
    event EpochSealed(uint256 indexed epochId, bytes32 merkleRoot, bytes32 ledgerDigest);
    event EpochAdvanced(uint256 indexed previousEpoch, uint256 indexed newEpoch, bytes32 node, bytes32 ledgerDigest);

    modifier onlyOwner() {
        require(msg.sender == owner, "EpochAuthority: owner only");
        _;
    }

    constructor(address owner_, uint256 initialEpoch, bytes32 initialLedgerDigest) {
        require(owner_ != address(0), "EpochAuthority: zero owner");
        require(initialEpoch > 0, "EpochAuthority: invalid epoch");
        require(initialLedgerDigest != bytes32(0), "EpochAuthority: zero ledger digest");
        owner = owner_;
        currentEpoch = initialEpoch;
        currentLedgerDigest = initialLedgerDigest;
        ledgerDigestOf[initialEpoch] = initialLedgerDigest;
        emit OwnershipTransferred(address(0), owner_);
    }

    function isEpochActive(uint256 epochId) public view override returns (bool) {
        return epochId == currentEpoch && !isEpochSealed[epochId];
    }

    function setLineageRegistry(address registry) external onlyOwner {
        require(address(lineageRegistry) == address(0), "EpochAuthority: registry already set");
        require(registry != address(0), "EpochAuthority: zero registry");
        lineageRegistry = ILineageRegistry(registry);
        emit LineageRegistrySet(registry);
    }

    function bindInitialLineage(bytes32 node) external onlyOwner {
        require(address(lineageRegistry) != address(0), "EpochAuthority: registry not set");
        require(node != bytes32(0), "EpochAuthority: zero node");
        lineageRegistry.bindLineage(currentEpoch, node);
        emit InitialLineageBound(currentEpoch, node);
    }

    function registerEpochClient(address client) external onlyOwner {
        require(client != address(0), "EpochAuthority: zero client");
        require(!isEpochClient[client], "EpochAuthority: client already registered");
        require(_epochClients.length < MAX_EPOCH_CLIENTS, "EpochAuthority: client limit reached");
        isEpochClient[client] = true;
        _epochClients.push(client);
        emit EpochClientRegistered(client);
    }

    function epochClientCount() external view returns (uint256) {
        return _epochClients.length;
    }

    function sealCurrentEpoch(bytes32 merkleRoot) external onlyOwner {
        require(isEpochActive(currentEpoch), "EpochAuthority: epoch not active");
        require(merkleRoot != bytes32(0), "EpochAuthority: zero Merkle root");
        lineageRegistry.anchorMerkleRoot(currentEpoch, merkleRoot);
        isEpochSealed[currentEpoch] = true;
        emit EpochSealed(currentEpoch, merkleRoot, currentLedgerDigest);
    }

    function advanceEpoch(bytes32 nextLedgerDigest, bytes32 nextLineageNode) external onlyOwner {
        require(isEpochSealed[currentEpoch], "EpochAuthority: current epoch not sealed");
        require(nextLedgerDigest != bytes32(0), "EpochAuthority: zero ledger digest");
        require(nextLineageNode != bytes32(0), "EpochAuthority: zero lineage node");

        uint256 previousEpoch = currentEpoch;
        uint256 nextEpoch = previousEpoch + 1;
        currentEpoch = nextEpoch;
        currentLedgerDigest = nextLedgerDigest;
        ledgerDigestOf[nextEpoch] = nextLedgerDigest;

        lineageRegistry.bindLineage(nextEpoch, nextLineageNode);
        for (uint256 i = 0; i < _epochClients.length; i++) {
            IEpochClient(_epochClients[i]).bindEpoch(nextEpoch, nextLineageNode);
        }

        emit EpochAdvanced(previousEpoch, nextEpoch, nextLineageNode, nextLedgerDigest);
    }

    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "EpochAuthority: zero owner");
        address oldOwner = owner;
        owner = newOwner;
        emit OwnershipTransferred(oldOwner, newOwner);
    }
}