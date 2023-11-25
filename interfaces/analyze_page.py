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
        # Cette fonction analyse les logs en fonction du chemin du fichier, du niveau de sévérité
        # et du nom du processus. Elle utilise les modules de l'application pour le traitement des logs.
        log_line_pattern = r'(\w+ +\d+ \d+:\d+:\d+) (\S+) (\S+): (.+)'
        parser = argparse.ArgumentParser(description='Parse and filter logs.')

        if self.log_file_path != "":
            parser.add_argument('--log_file', default=self.log_file_path, help='Chemin vers le fichier log')
        else:
            parser.add_argument('--log_file', default='/var/log/syslog', help='Chemin vers le fichier log par défaut')

        parser.add_argument('--severity', nargs='+', default=[], help='Spécifier les niveaux de sévérité à afficher')
        parser.add_argument('--process', default='', help='Spécifier le nom du processus pour filtrer les logs')

        args = parser.parse_args()
        log_file_path = args.log_file
        severity_levels = args.severity
        process_name = args.process

        log_parser = lp.LogParser(log_line_pattern)
        log_analyzer = la.LogAnalyzer()
        log_manager = lm.LogManager()

        log_reader = lr.LogReader()
        log_filter = lf.LogFilter()

        # Initialiser parsed_logs avec une liste vide
        parsed_logs = []

        parsed_logs = log_reader.read_log_file(log_file_path, log_parser)
        log_text = ""

        # TODO fixer ça
        # Problème dans ce if :  severity et proces_name c'est les variables que je récupére depuis le form
        # Voir comment rentrer dans le IF et comment fonctionne le tri


        # Filtrer les logs en fonction de la sévérité et du processus (si fournis)
        if severity != "" or process_name != "":
            filtered_logs = log_filter.filter_logs(parsed_logs, severity, process)
            log_text = "\n".join(self.format_log_entry(log) for log in filtered_logs)
        else:
            log_text = "\n".join(self.format_log_entry(log) for log in parsed_logs)
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
