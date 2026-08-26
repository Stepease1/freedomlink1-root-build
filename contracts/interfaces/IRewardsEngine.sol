// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IRewardsEngine {
    function applyBonusCodeReward(
        address user,
        uint8 rewardType,
        uint256 rewardValue,
        bytes32 codeHash
    ) external;
}
