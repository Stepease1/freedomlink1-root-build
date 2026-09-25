// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "../interfaces/IFL1C.sol";

interface IFL1CGovernanceRouter {
    function isAuthorized(address account) external view returns (bool);
}

interface IFL1CEpochManager {}

interface IFL1CLineageRegistry {
    function registerEvent(string calldata eventName, uint256 timestamp) external;
}

interface IFL1CCreatorIdentityRegistry {
    function bindCreator(address creatorAddress) external;
}

interface IFL1CRootstoneBinding {
    function bind(address identity) external;
}

contract FL1C is IFL1C {
    string public constant name = "Freedomlink1 Credit";
    string public constant symbol = "FL1C";
    uint8 public constant decimals = 18;

    uint256 public totalSupply;
    mapping(address => uint256) public balanceOf;

    IFL1CGovernanceRouter public governance;
    IFL1CEpochManager public epochs;
    IFL1CLineageRegistry public lineage;
    IFL1CCreatorIdentityRegistry public identity;
    IFL1CRootstoneBinding public rootstone;

    address public immutable creator;

    constructor(
        address _governance,
        address _epochs,
        address _lineage,
        address _identity,
        address _rootstone
    ) {
        governance = IFL1CGovernanceRouter(_governance);
        epochs = IFL1CEpochManager(_epochs);
        lineage = IFL1CLineageRegistry(_lineage);
        identity = IFL1CCreatorIdentityRegistry(_identity);
        rootstone = IFL1CRootstoneBinding(_rootstone);

        creator = msg.sender;

        lineage.registerEvent("FL1C Token Genesis", block.timestamp);
        identity.bindCreator(msg.sender);
        rootstone.bind(msg.sender);
    }

    function mint(address to, uint256 amount) external override {
        require(governance.isAuthorized(msg.sender), "Not authorized");
        totalSupply += amount;
        balanceOf[to] += amount;
        emit Transfer(address(0), to, amount);
    }

    function transfer(address to, uint256 amount) external override returns (bool) {
        require(balanceOf[msg.sender] >= amount, "Insufficient balance");
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;
        emit Transfer(msg.sender, to, amount);
        return true;
    }
}
