# importer les bibliothéque
import tkinter as tk 
from datetime import datetime

# créer la fenetre 
fenetre = tk.Tk()

fenetre.title("Calendrier de Dylan")
fenetre.geometry("420x300")
fenetre.configure(bg="#172554")

# recupere la date actuelle
aujourdhui = datetime.now()

semaine = aujourdhui.isocalendar().week
jour = aujourdhui.day
mois = aujourdhui.month
annee = aujourdhui.year

# listes en fr
jours = [
    "lundi", "mardi", "mercredi","jeudi", "vendredi", "samedi", "dimanche"
]

mois_fr = [
    "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "decembre"

]

#trouvée les nom en fr 
nom_jour = jours[aujourdhui.weekday()]
nom_mois = mois_fr[mois - 1]

# affiche le titre
titre = tk.Label(
    fenetre,
    text="CALENDREIER DE DYLAN",
    font=("Ariel", 15, "bold"),
    fg="white",
    bg="#172554"
)

titre.pack(pady=15)

#afficher la semaine
texte_semaine = tk.Label(
    fenetre,
    text=f"SEMAINE {semaine}",
    font=("Arial", 30, "bold"),
    fg="yellow",
    bg="#172554"
)

texte_semaine.pack(pady=10)

#afficher la date
texte_date = tk.Label(
    fenetre,
    text=f"{nom_jour} {jour} {nom_mois} {annee}",
    font=("Arial", 18),
    fg="white",
    bg="#172554"
)

texte_date.pack(pady=10)

#lancé la fenetre
fenetre.mainloop()