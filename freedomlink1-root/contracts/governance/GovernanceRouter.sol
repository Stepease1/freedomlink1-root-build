// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "../interfaces/IGovernanceRouter.sol";

contract GovernanceRouter is IGovernanceRouter {
    struct Permissions {
        bool mint;
        bool burn;
        bool changeRole;
    }

    uint256 public constant MAX_BATCH_SYNC = 100;

    address public governanceAuthority;
    address public pendingGovernanceAuthority;
    address public owner;
    address public fl1c;
    address public epochManager;
    address public lineageRegistry;
    mapping(address => Permissions) private _permissions;

    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);
    event GovernanceAuthorityTransferProposed(
        address indexed currentAuthority,
        address indexed pendingAuthority
    );
    event GovernanceAuthorityTransferAccepted(
        address indexed previousAuthority,
        address indexed newAuthority
    );
    event GovernanceAuthorityTransferCancelled(address indexed cancelledAuthority);
    event GovernanceAction(
        bytes32 indexed actionType,
        address indexed actor,
        address indexed target,
        uint256 batchSize
    );
    event PermissionsUpdated(
        address indexed account,
        bool canMint,
        bool canBurn,
        bool canChangeRole
    );

    modifier onlyOwner() {
        require(msg.sender == governanceAuthority, "GovernanceRouter: owner only");
        _;
    }

    constructor(
        address governanceAuthority_,
        address fl1c_,
        address epochManager_,
        address lineageRegistry_
    ) {
        require(governanceAuthority_ != address(0), "GovernanceRouter: zero authority");
        require(fl1c_ != address(0), "GovernanceRouter: zero FL1C");
        require(epochManager_ != address(0), "GovernanceRouter: zero epoch manager");
        require(lineageRegistry_ != address(0), "GovernanceRouter: zero lineage registry");

        governanceAuthority = governanceAuthority_;
        owner = governanceAuthority_;
        fl1c = fl1c_;
        epochManager = epochManager_;
        lineageRegistry = lineageRegistry_;
        emit OwnershipTransferred(address(0), governanceAuthority_);
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
        emit GovernanceAction(
            keccak256("PERMISSION_UPDATE"),
            msg.sender,
            account,
            1
        );
    }

    function batchSetPermissions(
        address[] calldata accounts,
        bool[] calldata mintPermissions,
        bool[] calldata burnPermissions,
        bool[] calldata rolePermissions
    ) external onlyOwner {
        uint256 length = accounts.length;
        require(length > 0, "GovernanceRouter: empty batch");
        require(length <= MAX_BATCH_SYNC, "GovernanceRouter: batch limit exceeded");
        require(
            mintPermissions.length == length &&
                burnPermissions.length == length &&
                rolePermissions.length == length,
            "GovernanceRouter: batch length mismatch"
        );

        for (uint256 i = 0; i < length; i++) {
            require(accounts[i] != address(0), "GovernanceRouter: zero account");
            _permissions[accounts[i]] = Permissions(
                mintPermissions[i],
                burnPermissions[i],
                rolePermissions[i]
            );
            emit PermissionsUpdated(
                accounts[i],
                mintPermissions[i],
                burnPermissions[i],
                rolePermissions[i]
            );
        }

        emit GovernanceAction(
            keccak256("BATCH_PERMISSION_UPDATE"),
            msg.sender,
            address(0),
            length
        );
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

    function proposeGovernanceAuthority(address newAuthority) external onlyOwner {
        require(newAuthority != address(0), "GovernanceRouter: zero authority");
        require(newAuthority != governanceAuthority, "GovernanceRouter: unchanged authority");
        pendingGovernanceAuthority = newAuthority;
        emit GovernanceAuthorityTransferProposed(governanceAuthority, newAuthority);
        emit GovernanceAction(
            keccak256("AUTHORITY_TRANSFER_PROPOSED"),
            msg.sender,
            newAuthority,
            1
        );
    }

    function acceptGovernanceAuthority() external {
        require(pendingGovernanceAuthority != address(0), "GovernanceRouter: no pending authority");
        require(msg.sender == pendingGovernanceAuthority, "GovernanceRouter: pending authority only");

        address previousAuthority = governanceAuthority;
        governanceAuthority = pendingGovernanceAuthority;
        owner = pendingGovernanceAuthority;
        pendingGovernanceAuthority = address(0);

        emit OwnershipTransferred(previousAuthority, governanceAuthority);
        emit GovernanceAuthorityTransferAccepted(previousAuthority, governanceAuthority);
        emit GovernanceAction(
            keccak256("AUTHORITY_TRANSFER_ACCEPTED"),
            msg.sender,
            governanceAuthority,
            1
        );
    }

    function cancelGovernanceAuthorityTransfer() external onlyOwner {
        address cancelledAuthority = pendingGovernanceAuthority;
        require(cancelledAuthority != address(0), "GovernanceRouter: no pending authority");
        pendingGovernanceAuthority = address(0);
        emit GovernanceAuthorityTransferCancelled(cancelledAuthority);
        emit GovernanceAction(
            keccak256("AUTHORITY_TRANSFER_CANCELLED"),
            msg.sender,
            cancelledAuthority,
            1
        );
    }

    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "GovernanceRouter: zero authority");
        require(newOwner != governanceAuthority, "GovernanceRouter: unchanged authority");
        pendingGovernanceAuthority = newOwner;
        emit GovernanceAuthorityTransferProposed(governanceAuthority, newOwner);
        emit GovernanceAction(
            keccak256("AUTHORITY_TRANSFER_PROPOSED"),
            msg.sender,
            newOwner,
            1
        );
    }
}