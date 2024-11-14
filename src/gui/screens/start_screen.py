import tkinter as tk
from tkinter import messagebox

class StartScreen(tk.Frame):
    def __init__(self, main_window, *args, **kwargs):
        super().__init__(main_window, *args, **kwargs)
        self.main_window = main_window
        self.configure(bg="#D3D3D3")
        self.create_widgets()

    def create_widgets(self):
        # Etiqueta de título
        title_label = tk.Label(self, text="Contract Analyzer", font=("Arial", 24, "bold"), bg="#D3D3D3")
        title_label.pack(pady=20)

        # Botón de Start
        start_button = tk.Button(self, text="Start", font=("Arial", 14), bg="green", fg="white", command=self.start_analysis)
        start_button.pack(pady=10)

        # Botón de Exit
        exit_button = tk.Button(self, text="Exit", font=("Arial", 14), bg="red", fg="white", command=self.exit_application)
        exit_button.pack(pady=10)

    def start_analysis(self):
        self.main_window.show_contract_selection_screen()

    def exit_application(self):
        # Mensaje de confirmación para salir de la aplicación
        if messagebox.askokcancel("Exit", "Are you sure you want to exit?"):
            self.main_window.destroy()
