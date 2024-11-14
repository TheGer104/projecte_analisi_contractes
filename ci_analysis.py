import os
import json
from src.utils.data_handler import DataHandler
from src.analysis.contract_analyzer import ContractAnalyzer
from src.reports.report_generator import ReportGenerator
from src.config.config_loader import load_config

def list_contracts(directory):
    """Lista los contratos disponibles en el directorio especificado."""
    return [f for f in os.listdir(directory) if f.endswith('.sol')]

def ci_analysis():
    # Cargar la configuración
    config = load_config()

    # Directorio de contratos (ajusta la ruta según la estructura de tu proyecto)
    contracts_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../tests/contracts'))

    # Verificar si existe el directorio de contratos
    if not os.path.exists(contracts_dir):
        print(f"El directorio '{contracts_dir}' no existe.")
        return

    # Listar contratos disponibles
    contracts = list_contracts(contracts_dir)
    if not contracts:
        print("No se encontraron contratos para analizar.")
        return

    # Seleccionar el primer contrato como ejemplo o modificar para seleccionar dinámicamente
    for contract_name in contracts:
        contract_path = os.path.join(contracts_dir, contract_name)
        print(f"Analizando contrato: {contract_name}")

        # Cargar el código del contrato
        data_handler = DataHandler(config)
        contract_code = data_handler.load_contract(contract_path)

        # Crear instancia del analizador de contratos
        contract_analyzer = ContractAnalyzer(config)

        # Ejecutar el análisis completo (análisis básico + análisis con Mythril)
        analysis_results = contract_analyzer.complex_analysis(contract_code, contract_path)

        # Guardar los resultados en formato JSON para el CI/CD
        output_path = config["output_path"]
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Generar el reporte en el formato deseado
        report_generator = ReportGenerator(config)
        report_generator.generate_report(analysis_results, format="json")
        print(f"Reporte generado en formato JSON para {contract_name}")

if __name__ == "__main__":
    ci_analysis()
