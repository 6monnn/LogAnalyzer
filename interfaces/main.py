import tkinter as tk
from welcome_page import WelcomePage
from ..app.log_parser import *
from ..app.log_manager import *
from ..app.log_analyzer import *
from ..app.log_reader import *
from .. app.log_filter import *


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.welcome_page = WelcomePage(self)
        # self.another_page = AnotherPage(self)
        # Ajoutez d'autres pages au besoin

        self.show_page("WelcomePage")

    def show_page(self, page_name):
        if page_name == "WelcomePage":
            self.welcome_page.pack()
            # Masquer les autres pages si nécessaire
        elif page_name == "AnotherPage":
            # Masquer la page d'accueil et afficher une autre page
            self.welcome_page.pack_forget()
            # self.another_page.pack()

if __name__ == "__main__":
    app = MainApplication()
    app.title("Log Analyzer")  # Set the title here
    app.geometry("600x200")  # Set the window size if needed
    app.mainloop()
