import json
import re
import subprocess
import pdb
import os 
import shutil

class ContractAnalyzer:
    def __init__(self, config):
        self.config = config
        # Detecta la ruta de mythril en el sistema
        self.mythril_path = shutil.which("myth")
        if not self.mythril_path:
            raise ValueError("Mythril no está instalado o no está en el PATH.")
    
    def __init__(self, config):
        self.config = config
        self.mythril_path = config.get("mythril_path")
        if not self.mythril_path:
            raise ValueError("The 'mythril_path' is not set in the configuration file. Please specify the full path to the Mythril executable.")

    def static_analysis(self, contract_code):
        findings = {}
        findings['length_check'] = len(contract_code) > 0
        findings['has_fallback'] = bool(re.search(r'\bfallback\s*\(\s*\)', contract_code))
        findings['uses_require_or_assert'] = bool(re.search(r'require|assert', contract_code))
        return {"static_analysis": findings}

    def symbolic_analysis(self, contract_code):
        findings = {}
        findings['complexity'] = contract_code.count('{') > 3
        return {"symbolic_analysis": findings}

    def dynamic_analysis(self, contract_code):
        findings = {}
        findings['loops'] = bool(re.search(r'\bwhile\s*\(|\bfor\s*\(', contract_code))
        return {"dynamic_analysis": findings}

    def detect_vulnerabilities(self, contract_code):
        findings = {}
        findings['reentrancy_vulnerable'] = bool(re.search(r'call(\.value|\{value\s*:\s*)', contract_code))
        findings['integer_overflow'] = bool(re.search(r'\+\s*=', contract_code))
        findings['tx_origin'] = bool(re.search(r'tx\.origin', contract_code))
        return {"vulnerabilities": findings}

    def full_analysis(self, contract_code):
        results = {}
        results.update(self.static_analysis(contract_code))
        results.update(self.symbolic_analysis(contract_code))
        results.update(self.dynamic_analysis(contract_code))
        results.update(self.detect_vulnerabilities(contract_code))
        return results
    
    def basic_analysis(self, contract_code):
        # Realiza los análisis estático, simbólico, dinámico y de vulnerabilidades
        results = {}
        results.update(self.static_analysis(contract_code))
        results.update(self.symbolic_analysis(contract_code))
        results.update(self.dynamic_analysis(contract_code))
        results.update(self.detect_vulnerabilities(contract_code))
        return results

    def complex_analysis(self, contract_code, contract_path):
        # Realiza el análisis estático, simbólico, dinámico y de vulnerabilidades
        analysis_results = self.full_analysis(contract_code)

        # Añade los resultados de Mythril al análisis
        mythril_results = self.analyze_with_mythril(contract_path)
        analysis_results["mythril_analysis"] = mythril_results  

        return analysis_results

    def analyze_with_mythril(self, contract_path):
        """Run Mythril analysis on the selected contract."""
        print(f"Running Mythril analysis on {contract_path}...")
        try:
            # Usa la ruta de 'myth' encontrada en el PATH
            result = subprocess.check_output(
                [self.mythril_path, "-x", contract_path],
                stderr=subprocess.STDOUT,
                text=True
            )

            # Intenta decodificar el resultado como JSON
            try:
                mythril_output = json.loads(result)
                print("Mythril analysis completed with JSON output.")
                return {"mythril_analysis": mythril_output} if "issues" in mythril_output else {"mythril_analysis": {"success": True, "issues": []}}
            except json.JSONDecodeError:
                # Si falla la decodificación, muestra la salida en texto
                print("Error decoding JSON from Mythril output, outputting as text.")
                return {"mythril_analysis": {"success": False, "raw_output": result}}

        except subprocess.CalledProcessError as e:
            print("Analysis completed with error.")
            try:
                # Intenta decodificar la salida de error como JSON
                mythril_output = json.loads(e.output)
                return {"mythril_analysis": mythril_output} if "issues" in mythril_output else {"mythril_analysis": {"success": True, "issues": []}}
            except json.JSONDecodeError:
                # En caso de error de JSON, devuelve la salida como texto
                print("Error decoding JSON from Mythril error output.")
                return {"mythril_analysis": {"success": False, "raw_output": e.output}}



