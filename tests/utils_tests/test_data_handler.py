import unittest
import json
from src.utils.data_handler import DataHandler
from src.config.config_loader import load_config
import os

class TestDataHandler(unittest.TestCase):
    def setUp(self):
        config = load_config()
        self.data_handler = DataHandler(config)
        self.test_data = {"test_key": "test_value"}
        self.json_path = 'test_report.json'
        self.csv_path = 'test_report.csv'
        self.html_path = 'test_report.html'
        self.contract_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','tests' ,'contracts', 'OverFlowVulnerableContract.sol'))

    def test_load_contract(self):
        # Aquí estamos asumiendo que la función load_contract en DataHandler
        # carga el contrato desde el archivo especificado y devuelve su contenido
        contract_data = self.data_handler.load_contract(self.contract_path)
        
        # Verificamos que el contrato se ha cargado correctamente
        # la función load_contract y los datos que devuelve
        self.assertIsNotNone(contract_data)
        self.assertIn("pragma solidity", contract_data)  

if __name__ == '__main__':
    unittest.main()
