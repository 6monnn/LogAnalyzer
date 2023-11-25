import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os

class WelcomePage(tk.Frame):
    def __init__(self, master=None, style=None):
        super().__init__(master, style=style)
        self.master = master
        self.style = ttk.Style()
        self.style.configure("TLabel", background="#336699", foreground="white", font=('Helvetica', 18, 'bold'))
        self.style.configure("TButton", background="#4caf50", foreground="white", font=('Helvetica', 14, 'bold'))

        self.create_widgets()

    def set_default_path(self):
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        self.file_path.set(desktop_path)

    def browse_file(self):
        default_file = "/var/log/syslog"
        file_path = filedialog.askopenfilename(initialdir=default_file, title="Select Log File")
        if file_path:
            self.file_path.set(file_path)

    def start_analysis(self):
        log_file_path = self.file_path.get()
        print(log_file_path)
        self.master.show_analyze_page(log_file_path)

    def create_widgets(self):
        # Set column and row weights to make the grid responsive
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        title_frame = ttk.Frame(self, style="TFrame")
        title_frame.pack(fill="both", expand=True)

        self.title_label = ttk.Label(title_frame, text="Welcome to Log Analyzer")
        self.title_label.pack(pady=10)

        entry_frame = ttk.Frame(self, style="TFrame")
        entry_frame.pack(fill="both", expand=True)

        self.file_path = tk.StringVar()
        self.set_default_path()

        self.file_entry = ttk.Entry(entry_frame, textvariable=self.file_path, width=50)
        self.file_entry.pack(side="left", padx=10, pady=10, fill="both")

        self.browse_button = ttk.Button(entry_frame, text="Browse", command=self.browse_file)
        self.browse_button.pack(side="left", padx=10, pady=10, fill="both")

        self.start_button = ttk.Button(self, text="Start Analysis", command=self.start_analysis)
        self.start_button.pack(fill="both", pady=20)

