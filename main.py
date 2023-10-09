import flet as f

def main(page: f.Page):
    ## Page Champs de saisie
    # Alert Dialog
    EmptyTaskName = f.AlertDialog(
        title=f.Text("Entrez un nom pour la tâche")
    )
    def open_dlg(e):
        page.dialog = EmptyTaskName
        EmptyTaskName.open = True
        page.update()
    # Bouton ajouter la tache
    def add_clicked(e):
        if new_task.value==(""):
            open_dlg(e)
        else:
            page.add(f.Checkbox(label=new_task.value))
            new_task.value = ("")
            page.update()

    # Champ de saisie nom de la tache
    new_task = f.TextField(hint_text="Nouvelle tâche", expand=True)
    # Champ de saisie nom de la personne
    # Menu dropdown importance de la tache
    # Menu dropdown etiquette
    # Menu selection de la date

    ## Page Liste des taches
    tasks_view = f.Column()
    # Tache
    # Coche tache effectuée

    ## Page principale
    # ALL
    view = f.Column(
        width=600,
        controls=[
            f.Row(
                controls=[
                    new_task,
                    f.FloatingActionButton(icon=f.icons.ADD, on_click=add_clicked),
                ],
            ),
            tasks_view,
        ],
    )
    page.horizontal_alignment = f.CrossAxisAlignment.CENTER
    page.add(view)

f.app(target=main)

