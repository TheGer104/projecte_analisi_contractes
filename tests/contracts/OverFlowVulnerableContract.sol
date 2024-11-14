pragma solidity ^0.5.0;

contract OverFlowVulnerableContract {
    address public owner;
    mapping(address => uint256) public balances;

    constructor() public {
        owner = msg.sender;
    }

    // Función vulnerable a un desbordamiento de enteros
    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    // Función vulnerable a desbordamiento intencional
    function withdraw(uint256 amount) public {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] -= amount;
        msg.sender.transfer(amount);
    }

    // Esta función aumenta el saldo del usuario sin control adecuado
    function unsafeIncrement(uint256 amount) public {
        balances[msg.sender] += amount; // Vulnerabilidad de desbordamiento de enteros
    }
}
