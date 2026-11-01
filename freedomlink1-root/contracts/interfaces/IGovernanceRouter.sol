// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IGovernanceRouter {
    function canMint(address caller) external view returns (bool);
    function canBurn(address caller) external view returns (bool);
    function canChangeRole(address caller) external view returns (bool);
}