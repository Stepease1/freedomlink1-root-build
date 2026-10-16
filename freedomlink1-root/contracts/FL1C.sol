// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "../interfaces/IFL1C.sol";

interface IRootstone {
    function isVerified(address subject) external view returns (bool);
}

interface IFL1CLineageRegistry {
    function registerEvent(string calldata eventName, uint256 timestamp) external;
}

contract FL1C is IFL1C {
    mapping(address => Role) private _roles;
    mapping(address => uint256) private _balances;

    address public override governanceRouter;
    address public override epochAuthority;
    address public override rootstoneRegistry;
    address public override lineageRegistry;

    uint256 public override currentEpoch;
    bytes32 public override lineageNode;

    modifier onlyGovernance() {
        require(
            msg.sender == governanceRouter || msg.sender == epochAuthority,
            "FL1C: governance only"
        );
        _;
    }

    modifier onlyRootstoneVerified(address subject) {
        require(
            IRootstone(rootstoneRegistry).isVerified(subject),
            "FL1C: rootstone verification failed"
        );
        _;
    }

    constructor(
        address _governanceRouter,
        address _epochAuthority,
        address _rootstoneRegistry,
        address _lineageRegistry,
        uint256 _epochId,
        bytes32 _lineageNode
    ) {
        require(_governanceRouter != address(0), "FL1C: zero governance router");
        require(_epochAuthority != address(0), "FL1C: zero epoch authority");
        require(_rootstoneRegistry != address(0), "FL1C: zero rootstone registry");
        require(_lineageRegistry != address(0), "FL1C: zero lineage registry");
        require(_epochId > 0, "FL1C: invalid epoch");
        require(_lineageNode != bytes32(0), "FL1C: empty lineage node");

        governanceRouter = _governanceRouter;
        epochAuthority = _epochAuthority;
        rootstoneRegistry = _rootstoneRegistry;
        lineageRegistry = _lineageRegistry;
        currentEpoch = _epochId;
        lineageNode = _lineageNode;

        emit EpochBound(_epochId, _lineageNode);
        _recordLineageEvent("FL1C Credential Genesis");
    }

    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function roleOf(address account) external view override returns (Role) {
        return _roles[account];
    }

    function mintCredential(address to, Role role, uint256 amount)
        external
        override
        onlyGovernance
        onlyRootstoneVerified(to)
    {
        require(to != address(0), "FL1C: zero recipient");
        require(role != Role.NONE, "FL1C: invalid role");
        require(amount > 0, "FL1C: zero amount");
        require(
            _roles[to] == Role.NONE || _roles[to] == role,
            "FL1C: role mismatch"
        );

        _balances[to] += amount;
        _roles[to] = role;
        emit CredentialMinted(to, role, amount, currentEpoch);
        _recordLineageEvent("FL1C Credential Minted");
    }

    function burnCredential(address from, uint256 amount) external override onlyGovernance {
        require(from != address(0), "FL1C: zero account");
        require(amount > 0, "FL1C: zero amount");
        require(_balances[from] >= amount, "FL1C: insufficient balance");

        Role role = _roles[from];
        _balances[from] -= amount;
        if (_balances[from] == 0) _roles[from] = Role.NONE;

        emit CredentialBurned(from, role, amount, currentEpoch);
        _recordLineageEvent("FL1C Credential Burned");
    }

    function changeRole(address account, Role newRole)
        external
        override
        onlyGovernance
        onlyRootstoneVerified(account)
    {
        require(account != address(0), "FL1C: zero account");
        require(_balances[account] > 0, "FL1C: no credential");
        require(newRole != Role.NONE, "FL1C: burn credential to revoke role");

        Role oldRole = _roles[account];
        require(oldRole != newRole, "FL1C: role unchanged");
        _roles[account] = newRole;

        emit RoleChanged(account, oldRole, newRole, currentEpoch);
        _recordLineageEvent("FL1C Credential Role Changed");
    }

    function bindEpoch(uint256 epochId, bytes32 newLineageNode) external override onlyGovernance {
        require(epochId > currentEpoch, "FL1C: epoch must advance");
        require(newLineageNode != bytes32(0), "FL1C: empty lineage node");

        currentEpoch = epochId;
        lineageNode = newLineageNode;
        emit EpochBound(epochId, newLineageNode);
        _recordLineageEvent("FL1C Epoch Bound");
    }

    function transfer(address, uint256) external pure override {
        revert("FL1C: transfer disabled");
    }

    function transferFrom(address, address, uint256) external pure override {
        revert("FL1C: transferFrom disabled");
    }

    function approve(address, uint256) external pure override {
        revert("FL1C: approve disabled");
    }

    function allowance(address, address) external pure override returns (uint256) {
        return 0;
    }

    function _recordLineageEvent(string memory eventName) private {
        IFL1CLineageRegistry(lineageRegistry).registerEvent(eventName, block.timestamp);
    }
}
