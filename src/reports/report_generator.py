import os
import json
import csv
import pandas as pd  

class ReportGenerator:
    
    def __init__(self, output_path, output_format="json"):
        self.output_path = output_path
        self.output_format = output_format

    def generate_report(self, analysis_results, contract_name):
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_filename = f"{contract_name}_{timestamp}.{self.output_format}"
        report_path = os.path.join(self.output_path, report_filename)

        if self.output_format == "json":
            with open(report_path, "w") as report_file:
                json.dump(analysis_results, report_file, indent=4)
            print(f"Reporte JSON generado en {report_path}")
        else:
            print("Formato de reporte no soportado actualmente.")


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
