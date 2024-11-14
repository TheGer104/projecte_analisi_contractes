import os
import json

from src.config.config_loader import load_config
from src.utils.data_handler import DataHandler
from src.analysis.contract_analyzer import ContractAnalyzer
from src.reports.report_generator import ReportGenerator
from src.gui.main_interface import MainWindow  # Importa la ventana principal de la interfaz gráfica


def main():
    app = MainWindow()
    app.mainloop()

if __name__ == "__main__":
    main()

'''
data_handler = DataHandler(config)
    contracts = data_handler.list_contracts(contracts_dir)
    
    if not contracts:
        print("No contracts found in the contracts directory.")
        return
    
    selected_contract = data_handler.select_contract(contracts)
    if not selected_contract:
        return

    contract_path = os.path.join(contracts_dir, selected_contract)
    contract_code = data_handler.load_contract(contract_path)

    contract_analyzer = ContractAnalyzer(config)
    analysis_results = contract_analyzer.full_analysis(contract_code)
    
    mythril_results = contract_analyzer.analyze_with_mythril(contract_path)
    analysis_results["mythril_analysis"] = mythril_results  

    report_generator = ReportGenerator(config)
    print("Select report format:")
    print("1. JSON")
    print("2. CSV")
    print("3. HTML")
    format_choice = input("Enter format (1-3): ")
    output_format = "json" if format_choice == "1" else "csv" if format_choice == "2" else "html"

    report_generator.generate_report(analysis_results, format=output_format)
    print(f"Report generated in {output_format} format in the reports directory.")

if __name__ == "__main__":
    main()
'''
    
