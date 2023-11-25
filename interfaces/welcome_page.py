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

        self.pack(fill="both", expand=True)
        self.create_widgets()

    def set_default_path(self):
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        self.file_path.set(desktop_path)

    def browse_file(self):
        self.file_path.set(filedialog.askopenfilename())

    def start_analysis(self):
        log_file_path = self.file_path.get()
        self.master.show_analyze_page(log_file_path)

    def create_widgets(self):
        # Set column and row weights to make the grid responsive
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        title_frame = ttk.Frame(self, style="TFrame")
        title_frame.grid(row=0, column=0, columnspan=2, sticky="nsew")

        self.title_label = ttk.Label(title_frame, text="Welcome to Log Analyzer")
        self.title_label.pack(pady=10)

        entry_frame = ttk.Frame(self, style="TFrame")
        entry_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

        self.file_path = tk.StringVar()
        self.set_default_path()

        self.file_entry = ttk.Entry(entry_frame, textvariable=self.file_path, width=50)
        self.file_entry.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        self.browse_button = ttk.Button(entry_frame, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        self.start_button = ttk.Button(self, text="Start Analysis", command=self.start_analysis)
        self.start_button.grid(row=2, column=0, columnspan=2, pady=20)
