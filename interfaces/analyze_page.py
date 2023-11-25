import tkinter as tk
import argparse
from tkinter import ttk
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
        log_text = f"Analyzing logs from: {self.log_file_path}"
        log_line_pattern = r'(\w+ +\d+ \d+:\d+:\d+) (\S+) (\S+): (.+)'

        parser = argparse.ArgumentParser(description='Parse and filter logs.')

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


        if severity_levels or process_name:
            filtered_logs = log_filter.filter_logs(parsed_logs, severity_levels, process_name)
            log_manager.display_logs(filtered_logs)
            log_text += "\n".join(filtered_logs)
        else:
            log_manager.display_logs(parsed_logs)
            log_text += "\n".join(parsed_logs)
            
        print(log_text)
        self.log_display.insert(tk.END, parsed_logs)

    def create_widgets(self):
        label = ttk.Label(self, text="Log Analysis Page")
        label.pack(pady=10)

        self.log_display = tk.Text(self, wrap="word", height=10, width=50)
        self.log_display.pack(padx=10, pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    analyze_page = AnalyzePage(root)
    analyze_page.set_log_file("/path/to/logfile.log")  # Replace with your actual log file path
    analyze_page.pack()
    root.mainloop()
