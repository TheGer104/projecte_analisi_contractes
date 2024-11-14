import tkinter as tk

class ContractSelectionScreen(tk.Frame):
    def __init__(self, parent, main_window, contracts):
        super().__init__(parent)
        self.main_window = main_window
        self.contracts = contracts
        self.configure(bg="#2E2E2E")

        title_label = tk.Label(self, text="Select Contract", font=("Arial", 18), bg="#2E2E2E", fg="white")
        title_label.pack(pady=20)

        for contract in self.contracts:
            contract_button = tk.Button(self, text=contract, command=lambda c=contract: self.select_contract(c), bg="#4CAF50", fg="white")
            contract_button.pack(pady=10)

    def select_contract(self, contract):
        self.main_window.selected_contract = contract
        self.show_analysis_type_screen()

    def show_analysis_type_screen(self):
        self.clear_window()
        
        # Título de selección de análisis
        title_label = tk.Label(self, text="Select Analysis Type", font=("Arial", 18), bg="#2E2E2E", fg="white")
        title_label.pack(pady=20)

        # Botón para análisis básico
        basic_analysis_button = tk.Button(self, text="Basic Analysis", command=self.basic_analysis, bg="#2196F3", fg="white")
        basic_analysis_button.pack(pady=10)

        # Botón para análisis complejo
        complex_analysis_button = tk.Button(self, text="Complex Analysis", command=self.complex_analysis, bg="#FF5722", fg="white")
        complex_analysis_button.pack(pady=10)

    def basic_analysis(self):
        self.main_window.analysis_mode = "basic"
        self.main_window.show_report_format_screen()

    def complex_analysis(self):
        self.main_window.analysis_mode = "complex"
        self.main_window.show_report_format_screen()

    def clear_window(self):
        for widget in self.winfo_children():
            widget.destroy()
