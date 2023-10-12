import flet as f
import flet as ft


def main(page: f.Page):
    img = f.Image(
        src=f"/Users/gregory/PycharmProjects/SAE-piloter-un-projet-informatique/media/logo_night.png",
        height=200,
        width=200,
        fit=f.ImageFit.CONTAIN,
    )
    ## Appbar
    page.appbar = f.AppBar(
        leading_width=200,
        title=f.Image(f"https://github.com/IroN404/SAE-piloter-un-projet-informatique/blob/main/media/logo_day.png?raw=true",
                      height=95),
        toolbar_height=70,
        center_title=True,
        bgcolor=f.colors.SURFACE_VARIANT,
        actions=[
            f.IconButton(f.icons.WB_SUNNY_OUTLINED)
        ],
    )
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
    list = [ 'tache']


    def add_clicked(e):
        if new_task.value==(""):
            open_dlg(e)
        else:
            page.add(f.Checkbox(label=f'{new_task.value}  {priority_selector.value}  {tags_selector.value}' ))
            list.append(f'{new_task.value}')
            new_task.value = ("")
            page.update()
            # rafraichir l'app
            page.update()



    # Champ de saisie nom de la tache
    new_task = f.TextField(hint_text="Nouvelle tâche",label='nom de la tache', expand=True)
    # Champ de saisie nom de la personne
    person = f.TextField(hint_text="Nom de la personne",label='nom', expand=True)
    # Menu dropdown importance de la tache
    priority_selector = f.Dropdown(
        width=200,
        label="Priorité",
        hint_text="Niveau de priorité",
        options=[
            f.dropdown.Option("Urgent"),
            f.dropdown.Option("Important"),
            f.dropdown.Option("Normal"),
        ],
    )
    # Menu dropdown etiquette
    tags_selector = f.Dropdown(
        width=200,
        label="Etiquette",
        hint_text="Choisissez une étiquette",
        options=[
            f.dropdown.Option("Travail"),
            f.dropdown.Option("Ecole"),
            f.dropdown.Option("Activitée"),
            f.dropdown.Option("Autre"),
        ],
    )
    # Menu selection de la date


    ## Page Liste des taches
    tasks_view = f.Column()
    # Tache

    # Checkbox delete task
    def delete_task(e):
        tasks_view.controls.remove(e)
        page.update()

    # Checkbox tache effectuée



    # Coche tache effectuée

    ## Page principale
    # ALLs



    view = f.Column(
        width=600,
        controls=[
            f.Row(
                controls=[
                    new_task,

                ],
            ),
            f.Row(
                controls=[
                    person,
                    priority_selector,
                    tags_selector,
                    f.FloatingActionButton(icon=f.icons.ADD, on_click=add_clicked),
                ],
            ),
            tasks_view,
        ],
    )
    page.horizontal_alignment = f.CrossAxisAlignment.CENTER
    page.add(view)

f.app(target=main)

