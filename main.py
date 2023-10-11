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

    # Bouton ajouter la tâche
    def add_clicked(e):
        if new_task.value == "" or personne.value == "":
            open_dlg(e)
        else:
            task_text = f.Row([f.Checkbox(label=new_task.value), f.Text(personne.value)])
            tasks_view.add(task_text)
            new_task.value = ""
            personne.value = ""
            page.update()

    # Champ de saisie du nom de la tâche
    new_task = f.TextField(hint_text="Nouvelle tâche", expand=True)

    # Champ de saisie du nom de la personne
    personne = f.TextField(hint_text="Nom de la personne", expand=True)



    ## Page Liste des tâches
    tasks_view = f.Column()

    ## Page principale
    view = f.Column(
        width=600,
        controls=[
            f.Row(
                controls=[
                    new_task,
                    personne,
                    f.FloatingActionButton(icon=f.icons.ADD, on_click=add_clicked),
                ],
            ),
            tasks_view,
        ],
    )
    page.horizontal_alignment = f.CrossAxisAlignment.CENTER
    page.add(view)

f.app(target=main)
