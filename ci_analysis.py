import os
import json
from datetime import datetime
from src.analysis.contract_analyzer import ContractAnalyzer
from src.reports.report_generator import ReportGenerator
from src.config.config_loader import load_config

def ci_analysis():
    # Cargar la configuración
    config = load_config()

    # Inicializar los componentes necesarios
    report_output_dir = "reports"
    os.makedirs(report_output_dir, exist_ok=True)  # Crear carpeta "reports" si no existe

    contract_analyzer = ContractAnalyzer(config)
    report_generator = ReportGenerator(output_dir=report_output_dir, output_format="json")  

    contracts_dir = "tests/contracts"
    contract_files = [f for f in os.listdir(contracts_dir) if f.endswith('.sol')]

    for contract_file in contract_files:
        contract_path = os.path.join(contracts_dir, contract_file)
        
        # Leer el contenido del contrato
        with open(contract_path, 'r') as f:
            contract_code = f.read()

        print(f"Analizando contrato: {contract_file}")
        
        # Realizar el análisis básico
        basic_analysis_results = contract_analyzer.full_analysis(contract_code)
        
        # Realizar el análisis complejo (incluyendo Mythril)
        complex_analysis_results = contract_analyzer.complex_analysis(contract_code, contract_path)

        # Combinar ambos resultados
        analysis_results = {
            "basic_analysis": basic_analysis_results,
            "complex_analysis": complex_analysis_results
        }
        
        # Generar el reporte con la fecha y hora en el nombre
        contract_name = os.path.splitext(contract_file)[0]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_name = f"{contract_name}_{timestamp}"
        report_path = report_generator.generate_report(analysis_results, report_name)
        
        print(f"Reporte generado: {report_path}")

if __name__ == "__main__":
    ci_analysis()
