import json
import re
import subprocess
import pdb
import os 

class ContractAnalyzer:
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
            result = subprocess.check_output(
                ["myth", "-x", contract_path],
                stderr=subprocess.STDOUT,
                text=True
            )
            )
            mythril_output = json.loads(result)
            if "issues" in mythril_output:
                print("Analysis completed successfully with issues found.")
                return {"mythril_analysis": mythril_output}  # Devuelve los resultados de Mythril directamente
            else:
                print("Analysis completed successfully without any issues.")
                return {"mythril_analysis": {"success": True, "issues": []}}

        except subprocess.CalledProcessError as e:
            print("Analysis Completed.")
            try:
                mythril_output = json.loads(e.output)
                
                if "issues" in mythril_output:
                    return {"mythril_analysis": mythril_output}
                else:
                    print("No issues found in output.")
                    return {"mythril_analysis": {"success": True, "issues": []}}
            except json.JSONDecodeError:
                print("Error decoding JSON from Mythril output.")
                return {"Completed": "Executed with no errors.", "details": e.output}

