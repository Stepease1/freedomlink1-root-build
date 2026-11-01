// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IEpochAuthority {
    function currentEpoch() external view returns (uint256);
    function isEpochActive(uint256 epochId) external view returns (bool);
}