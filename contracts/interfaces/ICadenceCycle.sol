// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface ICadenceCycle {
    function registerBonusCodeEvent(
        address user,
        bytes32 codeHash,
        uint8 rewardType
    ) external;
}
