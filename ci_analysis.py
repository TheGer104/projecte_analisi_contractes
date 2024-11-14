import os
import json
from src.reports.report_generator import ReportGenerator
from src.analysis.contract_analyzer import ContractAnalyzer
from src.config.config_loader import load_config

def ci_analysis():
    config = load_config()
    contract_analyzer = ContractAnalyzer(config)
    report_generator = ReportGenerator(config["output_path"], config["output_format"])

    contracts_dir = "tests/contracts"  # Ajusta esta ruta si es necesario
    for contract_file in os.listdir(contracts_dir):
        if contract_file.endswith(".sol"):
            contract_path = os.path.join(contracts_dir, contract_file)
            print(f"Analizando contrato: {contract_file}")

            # Leer el código del contrato
            with open(contract_path, "r") as file:
                contract_code = file.read()

            # Realizar el análisis
            analysis_results = contract_analyzer.complex_analysis(contract_code, contract_path)

            # Extraer el nombre del contrato sin la extensión ".sol"
            contract_name = os.path.splitext(contract_file)[0]

            # Generar el reporte usando el nombre del contrato
            report_generator.generate_report(analysis_results, contract_name=contract_name)
            print(f"Reporte generado en formato {config['output_format']} para {contract_file}")

if __name__ == "__main__":
    ci_analysis()
