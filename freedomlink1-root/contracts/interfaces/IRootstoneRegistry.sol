// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IRootstoneRegistry {
    function isVerified(address subject) external view returns (bool);
    function attestationOf(address subject) external view returns (bytes32);
}