// contracts/ComingToken.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract ComingToken is ERC20 {
    // initialSupply will be in Wei
    constructor(uint256 initialSupply) ERC20("ComingToken", "CT") {
        _mint(msg.sender, initialSupply);
    }
}
