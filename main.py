import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from interfaces.welcome_page import WelcomePage
from interfaces.analyze_page import AnalyzePage
from interfaces.gptinterface import GPTPage  # Import GPTPage

class LogAnalyzerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Analyseur de logs ")
        self.geometry("800x800")

        # Initialisation des pages Welcome, Analyze, et GPT
        self.welcome_page = WelcomePage(self)
        self.analyze_page = AnalyzePage(self)
        self.gpt_page = GPTPage(self)  # Create an instance of GPTPage

        # Affiche la page d'accueil au démarrage de l'application
        self.show_page("WelcomePage")

    def show_page(self, page_name):
        if page_name == "WelcomePage":
            self.welcome_page.pack()
            self.analyze_page.pack_forget()
            self.gpt_page.pack_forget()
        elif page_name == "AnalyzePage":
            self.welcome_page.pack_forget()
            self.analyze_page.pack()
            self.gpt_page.pack_forget()
        elif page_name == "GPTPage":
            self.welcome_page.pack_forget()
            self.analyze_page.pack_forget()
            self.gpt_page.pack()

    def show_analyze_page(self, log_file_path, process, severity):
        try:
            # Appelle la fonction set_log_file de AnalyzePage pour initialiser et afficher les logs
            self.analyze_page.set_log_file(log_file_path, severity, process)
            # Affiche la page d'analyse
            self.show_page("AnalyzePage")
        except Exception as e:
            # En cas d'erreur, affiche un message d'erreur et retourne à la page d'accueil
            messagebox.showerror("Error", f"Error during analysis: {str(e)}")
            self.show_page("WelcomePage")

    def show_gpt_page(self, log_file_path, process, severity):
        try:
            self.gpt_page.set_log_file(log_file_path, severity, process)
            self.show_page("GPTPage")
        except Exception as e :
            messagebox.showerror("Error", f"Error during GPT analysis: {str(e)}")
            self.show_page("WelcomePage")


   

    def show_welcome_page(self):
        # Affiche la page d'accueil
        self.show_page("WelcomePage")

# Bloc d'exécution principal
if __name__ == "__main__":
    # Initialise l'application et lance la boucle principale
    app = LogAnalyzerApp()
    app.mainloop()
