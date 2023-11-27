import tkinter as tk
from tkinter import ttk
import argparse
from tkinter import messagebox
import app.log_filter as lf
import app.log_parser as lp
import app.log_reader as lr
import app.log_manager as lm
import app.log_analyzer as la
from app.log_reader import LogReaderError

class AnalyzePage(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.log_file_path = None
        self.create_widgets()

    def set_log_file(self, log_file_path, severity, process):
        # Cette fonction est appelée pour définir le chemin du fichier log et déclencher l'analyse.
        # Elle prend en paramètre le chemin du fichier log, le niveau de sévérité et le process.
        self.log_file_path = log_file_path
        self.analyze_logs(severity, process)

    def analyze_logs(self, severity, process):
        log_line_pattern = r'(\w+ +\d+ \d+:\d+:\d+) (\S+) (\S+): (.+)'

        log_file_path = self.log_file_path if self.log_file_path != "" else '/var/log/syslog'

        log_parser = lp.LogParser(log_line_pattern)
        log_analyzer = la.LogAnalyzer()
        log_manager = lm.LogManager()

        log_reader = lr.LogReader()
        log_filter = lf.LogFilter()

        parsed_logs = log_reader.read_log_file(log_file_path, log_parser)
        log_text = ""

        # Check if severity or process is provided and filter logs accordingly
        if severity or process:
            filtered_logs = log_filter.filter_logs(parsed_logs, [severity] if severity else [], process)
            log_text = "\n".join(self.format_log_entry(log) for log in filtered_logs)
        else:
            log_text = "\n".join(self.format_log_entry(log) for log in parsed_logs)

        # Display the logs
        self.log_display.delete(1.0, tk.END)  # Clear existing text
        self.log_display.insert(tk.END, log_text)

    def format_log_entry(self, log):
        # Formater une entrée de log pour l'affichage
        return f"Timestamp: {log['timestamp']}\n" \
               f"Device: {log['device']}\n" \
               f"Process: {log['process']}\n" \
               f"Severity: {log['severity']}\n" \
               f"Message: {log['message']}\n" \
               f"{'-' * 30}"

    def create_widgets(self):
        # Créer les widgets de l'interface utilisateur (UI) pour la page d'analyse
        label = ttk.Label(self, text="Vos logs")
        label.pack(pady=10)

        # Frame pour contenir à la fois le widget de texte et la barre de défilement
        text_frame = ttk.Frame(self)
        text_frame.pack(padx=10, pady=10, expand=True, fill="both")

        self.log_display = tk.Text(text_frame, wrap="word", height=50, width=90)
        self.log_display.pack(side="left", expand=True, fill="both")

        # Barre de défilement
        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=self.log_display.yview)
        scrollbar.pack(side="right", fill="y")
        self.log_display.config(yscrollcommand=scrollbar.set)
