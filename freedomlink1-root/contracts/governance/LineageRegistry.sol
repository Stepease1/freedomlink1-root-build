// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "../interfaces/IEpochAuthority.sol";
import "../interfaces/ILineageRegistry.sol";

contract LineageRegistry is ILineageRegistry {
    address public owner;
    IEpochAuthority public epochAuthority;
    mapping(uint256 => bytes32) private _lineageNodes;
    mapping(uint256 => bytes32) private _merkleRoots;

    event EpochAuthoritySet(address indexed epochAuthority);
    event LineageBound(uint256 indexed epochId, bytes32 indexed node);
    event MerkleRootAnchored(uint256 indexed epochId, bytes32 indexed root);

    modifier onlyOwner() {
        require(msg.sender == owner, "LineageRegistry: owner only");
        _;
    }

    modifier onlyEpochAuthority() {
        require(msg.sender == address(epochAuthority), "LineageRegistry: epoch authority only");
        _;
    }

    constructor(address owner_) {
        require(owner_ != address(0), "LineageRegistry: zero owner");
        owner = owner_;
    }

    function setEpochAuthority(address authority) external onlyOwner {
        require(address(epochAuthority) == address(0), "LineageRegistry: authority already set");
        require(authority != address(0), "LineageRegistry: zero authority");
        epochAuthority = IEpochAuthority(authority);
        emit EpochAuthoritySet(authority);
    }

    function getLineageNode(uint256 epochId) external view override returns (bytes32) {
        return _lineageNodes[epochId];
    }

    function getMerkleRoot(uint256 epochId) external view override returns (bytes32) {
        return _merkleRoots[epochId];
    }

    function bindLineage(uint256 epochId, bytes32 node) external override onlyEpochAuthority {
        require(epochAuthority.isEpochActive(epochId), "LineageRegistry: inactive epoch");
        require(node != bytes32(0), "LineageRegistry: zero node");
        require(_lineageNodes[epochId] == bytes32(0), "LineageRegistry: lineage already bound");
        _lineageNodes[epochId] = node;
        emit LineageBound(epochId, node);
    }

    function anchorMerkleRoot(uint256 epochId, bytes32 root) external override onlyEpochAuthority {
        require(epochAuthority.isEpochActive(epochId), "LineageRegistry: inactive epoch");
        require(root != bytes32(0), "LineageRegistry: zero root");
        require(_merkleRoots[epochId] == bytes32(0), "LineageRegistry: root already anchored");
        _merkleRoots[epochId] = root;
        emit MerkleRootAnchored(epochId, root);
    }
}