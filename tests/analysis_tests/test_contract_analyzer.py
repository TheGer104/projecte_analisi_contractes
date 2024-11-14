import unittest
from src.analysis.contract_analyzer import ContractAnalyzer
from src.utils.data_handler import DataHandler
from src.config.config_loader import load_config
import os

class TestContractAnalyzer(unittest.TestCase):
    def setUp(self):
        # Cargar configuración y crear instancias de las clases necesarias
        config = load_config()
        self.data_handler = DataHandler(config)
        self.contract_analyzer = ContractAnalyzer(config)
        
        # Cargar un contrato de ejemplo desde la carpeta 'contracts'
        self.contract_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','tests' ,'contracts', 'OverFlowVulnerableContract.sol'))
        self.contract_data = self.data_handler.load_contract(self.contract_path)

    def test_static_analysis(self):
        """Verifica que el análisis estático retorna las claves esperadas."""
        result = self.contract_analyzer.static_analysis(self.contract_data)
        self.assertIn('length_check', result['static_analysis'])
        self.assertIn('has_fallback', result['static_analysis'])
        self.assertIn('uses_require_or_assert', result['static_analysis'])

    def test_symbolic_analysis(self):
        """Verifica que el análisis simbólico retorna las claves esperadas."""
        result = self.contract_analyzer.symbolic_analysis(self.contract_data)
        self.assertIn('complexity', result['symbolic_analysis'])

    def test_dynamic_analysis(self):
        """Verifica que el análisis dinámico retorna las claves esperadas."""
        result = self.contract_analyzer.dynamic_analysis(self.contract_data)
        self.assertIn('loops', result['dynamic_analysis'])

    def test_vulnerability_detection(self):
        """Verifica que la detección de vulnerabilidades retorna las claves esperadas."""
        result = self.contract_analyzer.detect_vulnerabilities(self.contract_data)
        self.assertIn('reentrancy_vulnerable', result['vulnerabilities'])
        self.assertIn('integer_overflow', result['vulnerabilities'])
        self.assertIn('tx_origin', result['vulnerabilities'])

    def test_mythril_analysis(self):
        """Verifica que el análisis con Mythril se ejecuta sin errores y devuelve un resultado."""
        result = self.contract_analyzer.analyze_with_mythril(self.contract_path)
        self.assertIn('Completed', result)
        self.assertIn('details', result)

    def test_full_analysis(self):
        """Verifica que el análisis completo contiene todas las secciones esperadas."""
        result = self.contract_analyzer.full_analysis(self.contract_data)
        self.assertIn('static_analysis', result)
        self.assertIn('symbolic_analysis', result)
        self.assertIn('dynamic_analysis', result)
        self.assertIn('vulnerabilities', result)

if __name__ == '__main__':
    unittest.main()
