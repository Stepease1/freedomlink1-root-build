// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ILineageRegistry {
    function getLineageNode(uint256 epochId) external view returns (bytes32);
    function getMerkleRoot(uint256 epochId) external view returns (bytes32);
    function bindLineage(uint256 epochId, bytes32 node) external;
    function anchorMerkleRoot(uint256 epochId, bytes32 root) external;
}