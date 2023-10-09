import flet as f

def main(page: f.Page):
    ## Page Champs de saisie
    # Champ de saisie nom de la tache
    # Champ de saisie nom de la personne
    # Menu dropdown importance de la tache
    # Menu dropdown etiquette
    # Menu selection de la date

    ## Page Liste des taches
    # Tache
    # Coche tache effectuée

    ## Page principale
    # ALL
    page.add(f.InputBorder(value="Enter a Name"))
f.app(target=main)

