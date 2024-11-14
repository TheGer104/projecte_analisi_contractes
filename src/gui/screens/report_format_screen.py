import tkinter as tk

class ReportFormatScreen(tk.Frame):
    def __init__(self, parent, main_window):
        super().__init__(parent)
        self.main_window = main_window
        self.configure(bg="#2E2E2E")

        title_label = tk.Label(self, text="Select Report Format", font=("Arial", 18), bg="#2E2E2E", fg="white")
        title_label.pack(pady=20)

        json_button = tk.Button(self, text="JSON", command=lambda: self.select_format("json"), bg="#4CAF50", fg="white")
        json_button.pack(pady=10)

        csv_button = tk.Button(self, text="CSV", command=lambda: self.select_format("csv"), bg="#2196F3", fg="white")
        csv_button.pack(pady=10)

        html_button = tk.Button(self, text="HTML", command=lambda: self.select_format("html"), bg="#FF5722", fg="white")
        html_button.pack(pady=10)

    def select_format(self, format):
        self.main_window.report_format = format
        self.main_window.show_progress_screen()
