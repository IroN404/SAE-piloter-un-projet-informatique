import flet as f
import datetime


def main(page: f.Page):
    # Alert Dialog
    EmptyTaskName = f.AlertDialog(
        title=f.Text("Entrez un nom pour la tâche")
    )

    InvalidPriority = f.AlertDialog(
        title=f.Text("Priorité invalide")
    )

    # Fonction pour ouvrir la boîte de dialogue
    def open_dlg(e):
        page.dialog = EmptyTaskName
        EmptyTaskName.open = True
        page.update()

    def open_invalid_priority_dlg(e):
        page.dialog = InvalidPriority
        InvalidPriority.open = True
        page.update()

    # Bouton ajouter la tache
    def add_clicked(e):
        if new_task.value == "" or person_name.value == "" or priorite.value == "":
            open_dlg(e)  # Ouvre la boîte de dialogue si l'un des champs est vide
        else:
            # Récupérez la priorité saisie par l'utilisateur
            user_priority = priorite.value.strip().upper()

            # Liste des priorités autorisées
            allowed_priorities = ["P1", "P2", "P3", "P4","p1","p2","p3","p4"]

            # Vérifiez si la priorité saisie par l'utilisateur est valide
            if user_priority not in allowed_priorities:
                open_invalid_priority_dlg(e)  # Ouvre la boîte de dialogue si la priorité n'est pas valide
            else:
                # Ajoute une case à cocher avec le texte de la tâche et la priorité
                task_with_info = f.Checkbox(label=f"{new_task.value} - {person_name.value} - Priorité : {user_priority} - Date de création : {datetime.datetime.now().strftime('%d-%m-%Y')} - {date_debut.value}- {date_fin.value}")
                page.add(task_with_info)
                new_task.value = ""  # Réinitialise le champ de tâche
                person_name.value = ""  # Réinitialise le champ de nom de personne
                priorite.value = ""  # Réinitialise le champ de priorité
                page.update()

    # Champ de saisie nom de la tache
    new_task = f.TextField(hint_text="Nouvelle tâche")
    page.add(new_task, f.FloatingActionButton(icon=f.icons.ADD, on_click=add_clicked))

    # Champ de saisie nom de la personne
    person_name = f.TextField(hint_text="Nom de la personne")
    page.add(person_name)

    # Champ de saisie priorité de la tache
    priorite = f.TextField(hint_text="Priorité de la tâche")
    page.add(priorite)

    # Texte explicatif pour les priorités acceptées
    priority_info = f.Text("Priorités acceptées : P1, P2, P3, P4")
    page.add(priority_info)

    # Champ de saisie date de début
    date_debut = f.TextField(hint_text="Date de début")
    page.add(date_debut)

    # Champ de saisie date de fin
    date_fin = f.TextField(hint_text="Date de fin")
    page.add(date_fin)


# Appelle la fonction main lors de l'exécution de l'application
f.app(target=main)
