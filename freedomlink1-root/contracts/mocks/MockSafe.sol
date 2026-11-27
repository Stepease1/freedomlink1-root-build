// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract MockSafe {
    address public owner;

    constructor(address owner_) {
        require(owner_ != address(0), "MockSafe: zero owner");
        owner = owner_;
    }

    function execute(address target, bytes calldata data) external returns (bytes memory) {
        require(msg.sender == owner, "MockSafe: owner only");
        require(target != address(0), "MockSafe: zero target");

        (bool success, bytes memory result) = target.call(data);
        require(success, "MockSafe: execution failed");

        return result;
    }
}
