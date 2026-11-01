// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "../interfaces/IRootstoneRegistry.sol";

contract RootstoneRegistry is IRootstoneRegistry {
    address public owner;
    mapping(address => bytes32) private _attestations;

    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);
    event IdentityAttested(address indexed subject, bytes32 indexed attestationHash);
    event IdentityRevoked(address indexed subject, bytes32 previousAttestationHash);

    modifier onlyOwner() {
        require(msg.sender == owner, "RootstoneRegistry: owner only");
        _;
    }

    constructor(address owner_) {
        require(owner_ != address(0), "RootstoneRegistry: zero owner");
        owner = owner_;
        emit OwnershipTransferred(address(0), owner_);
    }

    function setAttestation(address subject, bytes32 attestationHash) external onlyOwner {
        require(subject != address(0), "RootstoneRegistry: zero subject");
        require(attestationHash != bytes32(0), "RootstoneRegistry: zero attestation");
        _attestations[subject] = attestationHash;
        emit IdentityAttested(subject, attestationHash);
    }

    function revokeAttestation(address subject) external onlyOwner {
        require(subject != address(0), "RootstoneRegistry: zero subject");
        bytes32 previous = _attestations[subject];
        require(previous != bytes32(0), "RootstoneRegistry: no attestation");
        delete _attestations[subject];
        emit IdentityRevoked(subject, previous);
    }

    function isVerified(address subject) external view override returns (bool) {
        return _attestations[subject] != bytes32(0);
    }

    function attestationOf(address subject) external view override returns (bytes32) {
        return _attestations[subject];
    }

    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "RootstoneRegistry: zero owner");
        address oldOwner = owner;
        owner = newOwner;
        emit OwnershipTransferred(oldOwner, newOwner);
    }
}