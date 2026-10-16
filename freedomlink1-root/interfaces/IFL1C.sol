// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IFL1C {
    enum Role {
        NONE,
        FOUNDER,
        AGENCY,
        TREASURY,
        EDITORIAL,
        ROOTSTONE,
        GOVERNANCE
    }

    event EpochBound(uint256 epochId, bytes32 lineageNode);
    event CredentialMinted(address indexed account, Role role, uint256 amount, uint256 epochId);
    event CredentialBurned(address indexed account, Role role, uint256 amount, uint256 epochId);
    event RoleChanged(address indexed account, Role oldRole, Role newRole, uint256 epochId);

    function governanceRouter() external view returns (address);
    function epochAuthority() external view returns (address);
    function rootstoneRegistry() external view returns (address);
    function lineageRegistry() external view returns (address);
    function currentEpoch() external view returns (uint256);
    function lineageNode() external view returns (bytes32);
    function balanceOf(address account) external view returns (uint256);
    function roleOf(address account) external view returns (Role);
    function mintCredential(address to, Role role, uint256 amount) external;
    function burnCredential(address from, uint256 amount) external;
    function changeRole(address account, Role newRole) external;
    function bindEpoch(uint256 epochId, bytes32 newLineageNode) external;
    function transfer(address to, uint256 amount) external;
    function transferFrom(address from, address to, uint256 amount) external;
    function approve(address spender, uint256 amount) external;
    function allowance(address owner, address spender) external view returns (uint256);
}
