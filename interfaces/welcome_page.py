import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import os
from tkinter import messagebox

class WelcomePage(tk.Frame):
    def __init__(self, master=None, style=None):
        super().__init__(master, style=style)
        self.master = master
        self.style = ttk.Style()

        # Configuration du style pour les labels et les boutons
        self.style.configure("TLabel", foreground="black", font=('Helvetica', 18, 'bold'))
        self.style.configure("TButton", foreground="black", font=('Helvetica', 14, 'bold'))

        self.create_widgets()

    def set_default_path(self):
        # Définir le chemin par défaut du fichier
        desktop_path = "/var/log/syslog"
        self.file_path.set(desktop_path)

    def browse_file(self):
        # Ouvrir une boîte de dialogue pour sélectionner un fichier
        default_file = "/var/log/syslog"
        file_path = filedialog.askopenfilename(initialdir=default_file, title="Select Log File")
        if file_path:
            self.file_path.set(file_path)

    def start_analysis(self):
        # Obtenir les valeurs des champs
        log_file_path = self.file_path.get()
        severity_filter = self.severity_filter.get()
        process_filter = self.process_filter.get()

        # Ajouter une vérification pour s'assurer que le fichier existe
        if not os.path.exists(log_file_path):
            messagebox.showerror("Error", f"Fichier introuvable: {log_file_path}")
            return

        # Appeler la fonction show_analyze_page du maître avec les paramètres nécessaires
        self.master.show_analyze_page(log_file_path, process_filter, severity_filter)

    def create_widgets(self):
        # Configurer les poids des colonnes et des lignes pour rendre la grille réactive
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)

        # Cadre pour le titre
        title_frame = ttk.Frame(self, style="TFrame")
        title_frame.pack(fill="both", expand=True)

        # Label du titre
        self.title_label = ttk.Label(title_frame, text="Bienvenue dans notre analyseur de logs")
        self.title_label.pack(pady=10)

        # Cadre pour les champs d'entrée
        entry_frame = ttk.Frame(self, style="TFrame")
        entry_frame.pack(fill="both", expand=True)

        # Labels et champs de texte pour la sévérité et le processus
        severity_label = ttk.Label(entry_frame, text="Severity:")
        severity_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")

        self.severity_filter = tk.StringVar()
        severity_entry = ttk.Entry(entry_frame, textvariable=self.severity_filter, width=20)
        severity_entry.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        process_label = ttk.Label(entry_frame, text="Process:")
        process_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")

        self.process_filter = tk.StringVar()
        process_entry = ttk.Entry(entry_frame, textvariable=self.process_filter, width=20)
        process_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Label et champ de texte pour le chemin du fichier
        file_label = ttk.Label(entry_frame, text="Log File:")
        file_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")

        self.file_path = tk.StringVar()
        self.set_default_path()

        self.file_entry = ttk.Entry(entry_frame, textvariable=self.file_path, width=40)
        self.file_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Bouton pour parcourir les fichiers
        self.browse_button = ttk.Button(entry_frame, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=2, column=2, padx=10, pady=10, sticky="w")

        # Bouton pour démarrer l'analyse
        self.start_button = ttk.Button(self, text="Start Analysis", command=self.start_analysis)
        self.start_button.pack(fill="both", pady=20)

        # Menu déroulant pour les types de logs
        log_type_label = ttk.Label(entry_frame, text="Type de Log:")
        log_type_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        self.log_type = tk.StringVar()
        log_type_options = ["Android", "Apache", "Linux", "Mac", "OpenSSH", "OpenStack", "Thunderbird", "Windows"]
        self.log_type_combobox = ttk.Combobox(entry_frame, textvariable=self.log_type, values=log_type_options, state="readonly")
        self.log_type_combobox.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        self.log_type_combobox.current(2)

        self.anomaly_detection_var = tk.BooleanVar()
        self.anomaly_detection_checkbox = tk.Checkbutton(entry_frame, text="Détection d'anomalies", variable=self.anomaly_detection_var)
        self.anomaly_detection_checkbox.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="w")

        self.start_button.pack_forget()
        self.start_button.pack(fill="both", pady=20)