// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "../interfaces/IFL1C.sol";
import "./interfaces/IEpochAuthority.sol";
import "./interfaces/IEpochClient.sol";
import "./interfaces/IGovernanceRouter.sol";
import "./interfaces/ILineageRegistry.sol";
import "./interfaces/IRootstoneRegistry.sol";

contract FL1C is IFL1C, IEpochClient {
    mapping(address => Role) private _roles;
    mapping(address => uint256) private _balances;

    address public override governanceRouter;
    address public override epochAuthority;
    address public override rootstoneRegistry;
    address public override lineageRegistry;

    uint256 public override currentEpoch;
    bytes32 public override lineageNode;

    modifier onlyRootstoneVerified(address subject) {
        require(
            IRootstoneRegistry(rootstoneRegistry).isVerified(subject),
            "FL1C: rootstone verification failed"
        );
        _;
    }

    constructor(
        address _governanceRouter,
        address _epochAuthority,
        address _rootstoneRegistry,
        address _lineageRegistry
    ) {
        require(_governanceRouter != address(0), "FL1C: zero governance router");
        require(_epochAuthority != address(0), "FL1C: zero epoch authority");
        require(_rootstoneRegistry != address(0), "FL1C: zero rootstone registry");
        require(_lineageRegistry != address(0), "FL1C: zero lineage registry");
        governanceRouter = _governanceRouter;
        epochAuthority = _epochAuthority;
        rootstoneRegistry = _rootstoneRegistry;
        lineageRegistry = _lineageRegistry;
        currentEpoch = IEpochAuthority(_epochAuthority).currentEpoch();
        require(
            IEpochAuthority(_epochAuthority).isEpochActive(currentEpoch),
            "FL1C: epoch not active"
        );
        lineageNode = ILineageRegistry(_lineageRegistry).getLineageNode(currentEpoch);
        require(lineageNode != bytes32(0), "FL1C: lineage node not bound");

        emit EpochBound(currentEpoch, lineageNode);
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
        onlyRootstoneVerified(to)
    {
        require(IGovernanceRouter(governanceRouter).canMint(msg.sender), "FL1C: governance only");
        _requireActiveEpoch();
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
    }

    function burnCredential(address from, uint256 amount) external override {
        require(IGovernanceRouter(governanceRouter).canBurn(msg.sender), "FL1C: governance only");
        _requireActiveEpoch();
        require(from != address(0), "FL1C: zero account");
        require(amount > 0, "FL1C: zero amount");
        require(_balances[from] >= amount, "FL1C: insufficient balance");

        Role role = _roles[from];
        _balances[from] -= amount;
        if (_balances[from] == 0) _roles[from] = Role.NONE;

        emit CredentialBurned(from, role, amount, currentEpoch);
    }

    function changeRole(address account, Role newRole)
        external
        override
        onlyRootstoneVerified(account)
    {
        require(IGovernanceRouter(governanceRouter).canChangeRole(msg.sender), "FL1C: governance only");
        _requireActiveEpoch();
        require(account != address(0), "FL1C: zero account");
        require(_balances[account] > 0, "FL1C: no credential");
        require(newRole != Role.NONE, "FL1C: burn credential to revoke role");

        Role oldRole = _roles[account];
        require(oldRole != newRole, "FL1C: role unchanged");
        _roles[account] = newRole;

        emit RoleChanged(account, oldRole, newRole, currentEpoch);
    }

    function bindEpoch(uint256 epochId, bytes32 newLineageNode)
        external
        override(IFL1C, IEpochClient)
    {
        require(msg.sender == epochAuthority, "FL1C: epoch authority only");
        require(IEpochAuthority(epochAuthority).currentEpoch() == epochId, "FL1C: epoch mismatch");
        require(IEpochAuthority(epochAuthority).isEpochActive(epochId), "FL1C: epoch not active");
        require(newLineageNode != bytes32(0), "FL1C: empty lineage node");
        require(
            ILineageRegistry(lineageRegistry).getLineageNode(epochId) == newLineageNode,
            "FL1C: lineage mismatch"
        );

        currentEpoch = epochId;
        lineageNode = newLineageNode;
        emit EpochBound(epochId, newLineageNode);
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

    function _requireActiveEpoch() private view {
        require(IEpochAuthority(epochAuthority).isEpochActive(currentEpoch), "FL1C: epoch not active");
    }
}
