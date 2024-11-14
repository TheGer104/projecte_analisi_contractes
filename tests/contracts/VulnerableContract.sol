// SPDX-License-Identifier: MIT
pragma solidity ^0.5.0;

contract VulnerableContract {
    address public owner;
    uint256 public balance;

    // Constructor sets the owner
    constructor() public {
        owner = msg.sender;
    }

    // Fallback function (this can be detected by `has_fallback`)
    function() external payable {
        balance += msg.value;
    }

    // Function vulnerable to reentrancy attack
    function withdraw(uint256 amount) public {
        require(msg.sender == owner, "Only owner can withdraw");
        (bool sent, ) = msg.sender.call.value(amount)(""); // potential reentrancy vulnerability
        require(sent, "Failed to send Ether");
    }

    // Function that might have an integer overflow/underflow (depending on the Solidity version)
    function incrementBalance(uint256 amount) public {
        balance += amount; // possible integer overflow in older Solidity versions
    }

    // Function that uses tx.origin, which is generally insecure
    function privilegedAction() public {
        require(tx.origin == owner, "Only owner can call this function");
        // Do something privileged
    }

    // Infinite loop function for testing dynamic analysis
    function infiniteLoop() public {
        while (true) {
            balance += 1; // loop to test detection
        }
    }
}
