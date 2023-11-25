import tkinter as tk
from tkinter import ttk
from interfaces.welcome_page import WelcomePage
from interfaces.analyze_page import AnalyzePage  # Adjust the import based on your actual file structure

class LogAnalyzerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Log Analyzer App")
        self.geometry("600x400")

        self.welcome_page = WelcomePage(self)
        self.analyze_page = AnalyzePage(self)

        self.show_page("WelcomePage")

    def show_page(self, page_name):
        if page_name == "WelcomePage":
            self.welcome_page.pack()
            self.analyze_page.pack_forget()
        elif page_name == "AnalyzePage":
            self.welcome_page.pack_forget()
            self.analyze_page.pack()

    def show_analyze_page(self, log_file_path):
        self.analyze_page.set_log_file(log_file_path)
        self.show_page("AnalyzePage")

if __name__ == "__main__":
    app = LogAnalyzerApp()
    app.mainloop()
