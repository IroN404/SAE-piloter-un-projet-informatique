import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime, timedelta

def afficher_calendrier():
    def appliquer_date():
        selected_date = cal.get_date()
        date_var.set(selected_date)
        fenetre_calendrier.destroy()

    fenetre_calendrier = tk.Toplevel()
    fenetre_calendrier.title("Sélection de date")
    cal = Calendar(fenetre_calendrier, selectmode="day", date_pattern="dd/MM/yyyy")
    cal.pack(padx=20, pady=20)
    
    bouton_appliquer = ttk.Button(fenetre_calendrier, text="Appliquer la date", command=appliquer_date)
    bouton_appliquer.pack()

# Créer une fenêtre tkinter
fenetre = tk.Tk()
fenetre.title("Sélection de date avec menu déroulant")

# Variable pour stocker la date sélectionnée
date_var = tk.StringVar()

# Obtenez la date actuelle
date_actuelle = datetime.now()

# Créez une liste de dates prédéfinies à partir de la date actuelle pour les 7 prochains jours
dates = [date_actuelle.strftime('%d/%m/%Y')]
for _ in range(1, 7):
    date_actuelle += timedelta(days=1)
    dates.append(date_actuelle.strftime('%d/%m/%Y'))

# Créer un menu déroulant avec les dates prédéfinies
date_menu = ttk.Combobox(fenetre, textvariable=date_var, values=dates)
date_menu.pack(padx=20, pady=20)

# Bouton pour afficher le calendrier
bouton_afficher = ttk.Button(fenetre, text="Afficher le calendrier", command=afficher_calendrier)
bouton_afficher.pack()

# Bouton pour appliquer la date sélectionnée
def appliquer_date_selectionnee():
    selected_date = date_menu.get()
    print("Date sélectionnée :", selected_date)

bouton_appliquer_date = ttk.Button(fenetre, text="Appliquer la date sélectionnée", command=appliquer_date_selectionnee)
bouton_appliquer_date.pack()

fenetre.mainloop()
