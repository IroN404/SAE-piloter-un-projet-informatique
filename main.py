import flet as f

def main(page: f.Page):
    # Alert Dialog
    EmptyTaskName = f.AlertDialog(
        title=f.Text("Entrez un nom pour la tâche")
    )

    # Fonction pour ouvrir la boîte de dialogue
    def open_dlg(e):
        page.dialog = EmptyTaskName
        EmptyTaskName.open = True
        page.update()

    # Bouton ajouter la tache
    def add_clicked(e):
        if new_task.value == "":
            open_dlg(e)  # Ouvre la boîte de dialogue si le champ est vide
        else:
            # Ajoute une case à cocher avec le texte entré dans le champ
            page.add(f.Checkbox(label=new_task.value))
            new_task.value = ""  # Réinitialise le champ de saisie
            page.update()

    # Champ de saisie nom de la tache
    new_task = f.TextField(hint_text="Nouvelle tâche")
    page.add(new_task, f.FloatingActionButton(icon=f.icons.ADD, on_click=add_clicked))



    # Champ de saisie nom de la personne (commentaire manquant)
    person_name = f.TextField(hint_text="Nom de la personne")
    page.add(person_name)

    # Menu dropdown importance de la tache (commentaire manquant)
    # Menu dropdown etiquette (commentaire manquant)
    # Menu selection de la date (commentaire manquant)

    ## Page Liste des taches

    # Tache (commentaire manquant)
    # Coche tache effectuée (commentaire manquant)

# Appelle la fonction main lors de l'exécution de l'application
f.app(target=main)
