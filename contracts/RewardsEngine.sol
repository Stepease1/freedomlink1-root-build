// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract RewardsEngine {

    address public system;

    modifier onlySystem() {
        require(msg.sender == system, "Not system");
        _;
    }

    constructor(address _system) {
        system = _system;
    }

    enum RewardType {
        BoostMultiplier,
        BadgeCredit,
        CadenceBoost,
        AccessPass,
        LineageMark
    }

    mapping(address => uint256) public userBoostMultiplier;
    mapping(address => uint256) public userBadgeProgress;
    mapping(address => uint256) public userCadenceScore;
    mapping(address => bool) public governanceAccess;
    mapping(address => uint256) public lineageMarks;

    event RewardApplied(address indexed user, RewardType rewardType, uint256 rewardValue, bytes32 codeHash);

    function applyBonusCodeReward(
        address user,
        uint8 rewardType,
        uint256 rewardValue,
        bytes32 codeHash
    ) external onlySystem {

        if (rewardType == uint8(RewardType.BoostMultiplier)) {
            userBoostMultiplier[user] += rewardValue;
        }
        else if (rewardType == uint8(RewardType.BadgeCredit)) {
            userBadgeProgress[user] += rewardValue;
        }
        else if (rewardType == uint8(RewardType.CadenceBoost)) {
            userCadenceScore[user] += rewardValue;
        }
        else if (rewardType == uint8(RewardType.AccessPass)) {
            governanceAccess[user] = true;
        }
        else if (rewardType == uint8(RewardType.LineageMark)) {
            lineageMarks[user] += rewardValue;
        }

        emit RewardApplied(user, RewardType(rewardType), rewardValue, codeHash);
    }
}
