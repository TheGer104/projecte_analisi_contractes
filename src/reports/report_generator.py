import os
import json
import csv
import pandas as pd  
from datetime import datetime

class ReportGenerator:
    
    def __init__(self, output_path, output_format="json"):
        self.output_path = output_path
        self.output_format = output_format
    
    def generate_report(self, analysis_results, contract_name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{contract_name}_{timestamp}.json"
        filepath = os.path.join(self.output_path, filename)

        # Si el archivo existe, lo elimina para permitir la sobrescritura
        if os.path.exists(filepath):
            os.remove(filepath)

        with open(filepath, "w") as report_file:
            json.dump(analysis_results, report_file, indent=4)

        print(f"Reporte generado en formato {self.output_format} para {contract_name}")


    def _generate_json_report(self, data):
        filepath = os.path.join(self.output_path, "report.json")
        with open(filepath, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Reporte JSON generado en {filepath}")

    def _generate_csv_report(self, data):
        filepath = os.path.join(self.output_path, "report.csv")
        # Convierte el diccionario de datos en una lista de pares clave-valor para CSV
        flat_data = self._flatten_data(data)
        with open(filepath, "w", newline="") as file:
            writer = csv.writer(file)
            for key, value in flat_data.items():
                writer.writerow([key, value])
        print(f"Reporte CSV generado en {filepath}")

    def _generate_html_report(self, data):
        filepath = os.path.join(self.output_path, "report.html")
        # Convierte el diccionario de datos en una tabla HTML usando pandas
        flat_data = self._flatten_data(data)
        df = pd.DataFrame(flat_data.items(), columns=["Key", "Value"])
        df.to_html(filepath, index=False)
        print(f"Reporte HTML generado en {filepath}")

    def _flatten_data(self, data, parent_key='', sep='_'):
        # Convierte el diccionario anidado en un formato plano para CSV y HTML
        items = []
        for k, v in data.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            if isinstance(v, dict):
                items.extend(self._flatten_data(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)
