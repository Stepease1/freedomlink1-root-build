// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract CadenceCycle {

    address public system;

    modifier onlySystem() {
        require(msg.sender == system, "Not system");
        _;
    }

    constructor(address _system) {
        system = _system;
    }

    struct CadenceEvent {
        uint64 timestamp;
        bytes32 codeHash;
        uint8 rewardType;
    }

    mapping(address => CadenceEvent[]) public userEvents;
    mapping(address => uint256) public userCadenceScore;

    event BonusCodeEventRegistered(address indexed user, bytes32 codeHash, uint8 rewardType);

    function registerBonusCodeEvent(
        address user,
        bytes32 codeHash,
        uint8 rewardType
    ) external onlySystem {

        userEvents[user].push(CadenceEvent({
            timestamp: uint64(block.timestamp),
            codeHash: codeHash,
            rewardType: rewardType
        }));

        userCadenceScore[user] += weightForRewardType(rewardType);

        emit BonusCodeEventRegistered(user, codeHash, rewardType);
    }

    function weightForRewardType(uint8 rewardType) internal pure returns (uint256) {
        if (rewardType == 0) return 5;
        if (rewardType == 1) return 3;
        if (rewardType == 2) return 10;
        if (rewardType == 3) return 20;
        if (rewardType == 4) return 50;
        return 1;
    }
}
