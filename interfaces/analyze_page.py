import tkinter as tk
from tkinter import ttk
import argparse
import app.log_filter as lf
import app.log_parser as lp
import app.log_reader as lr
import app.log_manager as lm
import app.log_analyzer as la

class AnalyzePage(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.log_file_path = None
        self.create_widgets()

    def set_log_file(self, log_file_path):
        self.log_file_path = log_file_path
        self.analyze_logs()

    def analyze_logs(self):
        log_line_pattern = r'(\w+ +\d+ \d+:\d+:\d+) (\S+) (\S+): (.+)'
        parser = argparse.ArgumentParser(description='Parse and filter logs.')

        if self.log_file_path != "":
            parser.add_argument('--log_file', default=self.log_file_path, help='Path to the log file')
        else:
            parser.add_argument('--log_file', default='/var/log/syslog', help='Path to the log file')

        parser.add_argument('--severity', nargs='+', default=[], help='Specify severity levels to display')
        parser.add_argument('--process', default='', help='Specify process name to filter logs')

        args = parser.parse_args()
        log_file_path = args.log_file
        severity_levels = args.severity
        process_name = args.process

        log_parser = lp.LogParser(log_line_pattern)
        log_analyzer = la.LogAnalyzer()
        log_manager = lm.LogManager()

        log_reader = lr.LogReader()
        log_filter = lf.LogFilter()

        parsed_logs = log_reader.read_log_file(log_file_path, log_parser)
        log_text = ""

        if severity_levels or process_name:
            filtered_logs = log_filter.filter_logs(parsed_logs, severity_levels, process_name)
            log_text = "\n".join(self.format_log_entry(log) for log in filtered_logs)
        else:
            log_text = "\n".join(self.format_log_entry(log) for log in parsed_logs)

        self.log_display.insert(tk.END, log_text)

    def format_log_entry(self, log):
        return f"Timestamp: {log['timestamp']}\n" \
               f"Device: {log['device']}\n" \
               f"Process: {log['process']}\n" \
               f"Severity: {log['severity']}\n" \
               f"Message: {log['message']}\n" \
               f"{'-' * 30}"

    def create_widgets(self):
        label = ttk.Label(self, text="Log Analysis Page")
        label.pack(pady=10)

        # Frame to contain both the text widget and the scrollbar
        text_frame = ttk.Frame(self)
        text_frame.pack(padx=10, pady=10, expand=True, fill="both")

        self.log_display = tk.Text(text_frame, wrap="word", height=20, width=80)
        self.log_display.pack(side="left", expand=True, fill="both")

        # Scrollbar
        scrollbar = ttk.Scrollbar(text_frame, orient="vertical", command=self.log_display.yview)
        scrollbar.pack(side="right", fill="y")
        self.log_display.config(yscrollcommand=scrollbar.set)
