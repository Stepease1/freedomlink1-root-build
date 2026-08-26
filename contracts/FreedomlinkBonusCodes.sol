// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "./interfaces/IRewardsEngine.sol";
import "./interfaces/ICadenceCycle.sol";

contract FreedomlinkBonusCodes {

    // ------------------------------------------------------------
    // Roles
    // ------------------------------------------------------------
    address public steward;
    mapping(address => bool) public custodians;

    modifier onlySteward() {
        require(msg.sender == steward, "Not steward");
        _;
    }

    modifier onlyCustodian() {
        require(custodians[msg.sender], "Not custodian");
        _;
    }

    // ------------------------------------------------------------
    // Reward Engine + Cadence Cycle
    // ------------------------------------------------------------
    IRewardsEngine public rewardsEngine;
    ICadenceCycle public cadenceCycle;

    function setRewardsEngine(address engine) external onlySteward {
        rewardsEngine = IRewardsEngine(engine);
    }

    function setCadenceCycle(address cycle) external onlySteward {
        cadenceCycle = ICadenceCycle(cycle);
    }

    // ------------------------------------------------------------
    // Bonus Code Storage
    // ------------------------------------------------------------
    struct Code {
        bool exists;
        bool redeemed;
        uint8 rewardType;
        uint256 rewardValue;
        uint64 expiresAt;
    }

    mapping(bytes32 => Code) public codes;

    // ------------------------------------------------------------
    // Events
    // ------------------------------------------------------------
    event CodeIssued(bytes32 indexed codeHash, uint8 rewardType, uint256 rewardValue, uint64 expiresAt);
    event CodeRedeemed(bytes32 indexed codeHash, address indexed user, uint8 rewardType, uint256 rewardValue);

    // ------------------------------------------------------------
    // Constructor
    // ------------------------------------------------------------
    constructor(address _steward) {
        steward = _steward;
        custodians[_steward] = true;
    }

    // ------------------------------------------------------------
    // Issue Code
    // ------------------------------------------------------------
    function issueCode(
        bytes32 codeHash,
        uint8 rewardType,
        uint256 rewardValue,
        uint64 expiresAt
    ) external onlyCustodian {
        require(!codes[codeHash].exists, "Already exists");

        codes[codeHash] = Code({
            exists: true,
            redeemed: false,
            rewardType: rewardType,
            rewardValue: rewardValue,
            expiresAt: expiresAt
        });

        emit CodeIssued(codeHash, rewardType, rewardValue, expiresAt);
    }

    // ------------------------------------------------------------
    // Redeem Code
    // ------------------------------------------------------------
    function redeemCode(string calldata rawCode) external {
        bytes32 codeHash = keccak256(bytes(rawCode));
        Code storage c = codes[codeHash];

        require(c.exists, "Invalid code");
        require(!c.redeemed, "Already redeemed");
        require(block.timestamp <= c.expiresAt, "Expired");

        c.redeemed = true;

        rewardsEngine.applyBonusCodeReward(msg.sender, c.rewardType, c.rewardValue, codeHash);
        cadenceCycle.registerBonusCodeEvent(msg.sender, codeHash, c.rewardType);

        emit CodeRedeemed(codeHash, msg.sender, c.rewardType, c.rewardValue);
    }

    // ------------------------------------------------------------
    // Admin
    // ------------------------------------------------------------
    function setCustodian(address custodian, bool status) external onlySteward {
        custodians[custodian] = status;
    }
}
