import unittest
import os
from src.reports.report_generator import ReportGenerator
from src.config.config_loader import load_config
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../src')))


class TestReportGenerator(unittest.TestCase):
    def setUp(self):
        config = load_config()
        self.report_generator = ReportGenerator(config)
        self.sample_data = {
            "static_analysis": {"length_check": True, "has_fallback": True, "uses_require_or_assert": True},
            "symbolic_analysis": {"complexity": True},
            "dynamic_analysis": {"loops": True},
            "vulnerabilities": {"reentrancy_vulnerable": True, "integer_overflow": True, "tx_origin": True}
        }
        # Define file paths for reports
        self.json_path = os.path.join(config['output_path'], "report.json")
        self.csv_path = os.path.join(config['output_path'], "report.csv")
        self.html_path = os.path.join(config['output_path'], "report.html")

    def test_save_as_json(self):
        self.report_generator.save_as_json(self.sample_data)
        self.assertTrue(os.path.isfile(self.json_path))

    def test_save_as_csv(self):
        self.report_generator.save_as_csv(self.sample_data)
        self.assertTrue(os.path.isfile(self.csv_path))

    def test_save_as_html(self):
        self.report_generator.save_as_html(self.sample_data)
        self.assertTrue(os.path.isfile(self.html_path))

    def tearDown(self):
        # Clean up generated files after tests
        for filepath in [self.json_path, self.csv_path, self.html_path]:
            if os.path.exists(filepath):
                os.remove(filepath)

if __name__ == '__main__':
    unittest.main()
