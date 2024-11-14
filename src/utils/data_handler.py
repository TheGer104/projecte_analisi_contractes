import json
import csv
import os

class DataHandler:
    def __init__(self, config):
        self.config = config

    def load_config(self, filepath):
        """Load configuration for analysis."""
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"Config file not found: {filepath}")
        
        with open(filepath, 'r') as file:
            config = json.load(file)
        
        return config

    def load_contract(self, filepath):
        """Load a smart contract from a file."""
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"Contract file not found: {filepath}")
        
        with open(filepath, 'r') as file:
            contract_code = file.read()
        
        return contract_code
    
    def list_contracts(self, directory):
        """List all Solidity (.sol) files in the contracts directory."""
        return [f for f in os.listdir(directory) if f.endswith('.sol')]

    def select_contract(self, contracts):
        """Allow the user to select a contract from the list."""
        print("Available contracts:")
        for idx, contract in enumerate(contracts, start=1):
            print(f"{idx}. {contract}")
        
        choice = int(input("Select a contract by number: ")) - 1
        if 0 <= choice < len(contracts):
            return contracts[choice]
        else:
            print("Invalid choice.")
            return None
