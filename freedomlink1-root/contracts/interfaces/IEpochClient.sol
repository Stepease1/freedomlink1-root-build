// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IEpochClient {
    function bindEpoch(uint256 epochId, bytes32 newLineageNode) external;
}