// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "../interfaces/IGovernanceRouter.sol";

contract GovernanceRouter is IGovernanceRouter {
    struct Permissions {
        bool mint;
        bool burn;
        bool changeRole;
    }

    address public owner;
    mapping(address => Permissions) private _permissions;

    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);
    event PermissionsUpdated(
        address indexed account,
        bool canMint,
        bool canBurn,
        bool canChangeRole
    );

    modifier onlyOwner() {
        require(msg.sender == owner, "GovernanceRouter: owner only");
        _;
    }

    constructor(address owner_) {
        require(owner_ != address(0), "GovernanceRouter: zero owner");
        owner = owner_;
        emit OwnershipTransferred(address(0), owner_);
    }

    function setPermissions(
        address account,
        bool mintPermission,
        bool burnPermission,
        bool rolePermission
    ) external onlyOwner {
        require(account != address(0), "GovernanceRouter: zero account");
        _permissions[account] = Permissions(mintPermission, burnPermission, rolePermission);
        emit PermissionsUpdated(account, mintPermission, burnPermission, rolePermission);
    }

    function canMint(address caller) external view override returns (bool) {
        return _permissions[caller].mint;
    }

    function canBurn(address caller) external view override returns (bool) {
        return _permissions[caller].burn;
    }

    function canChangeRole(address caller) external view override returns (bool) {
        return _permissions[caller].changeRole;
    }

    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "GovernanceRouter: zero owner");
        address oldOwner = owner;
        owner = newOwner;
        emit OwnershipTransferred(oldOwner, newOwner);
    }
}