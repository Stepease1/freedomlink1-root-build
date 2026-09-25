// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

interface IFL1C {
    event Transfer(address indexed from, address indexed to, uint256 value);

    function mint(address to, uint256 amount) external;
    function transfer(address to, uint256 amount) external returns (bool);
}
