import tkinter as tk
import json

class ResultsScreen(tk.Frame):
    def __init__(self, main_window, **kwargs):
        super().__init__(main_window, **kwargs)
        self.main_window = main_window
        self.create_widgets()

    def create_widgets(self):
        # Crear el área de texto para mostrar los resultados
        results_text = tk.Text(self, wrap="word", width=80, height=20)
        results_text.pack(padx=20, pady=20, fill="both", expand=True)

        # Insertar los resultados formateados en el área de texto
        formatted_results = self.format_results()
        results_text.insert(tk.END, formatted_results)

        # Botones de navegación
        menu_button = tk.Button(self, text="Menu", command=self.main_window.show_start_screen, bg="green", fg="white")
        menu_button.pack(side="left", padx=20, pady=20)

        exit_button = tk.Button(self, text="Exit", command=self.main_window.quit, bg="red", fg="white")
        exit_button.pack(side="right", padx=20, pady=20)

    def format_results(self):
        if not hasattr(self.main_window, 'analysis_results') or not self.main_window.analysis_results:
            return "No results available."

        # Intenta formatear los resultados en JSON legible
        try:
            formatted_results = json.dumps(self.main_window.analysis_results, indent=4)
            return formatted_results
        except TypeError as e:
            print(f"Error formatting results: {e}")
            return "Error displaying results."
