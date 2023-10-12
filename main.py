import flet as f

def main(page: f.Page):
    # Configuration de l'image
    img_path = "/Users/gregory/PycharmProjects/SAE-piloter-un-projet-informatique/media/logo_night.png"
    img = f.Image(src=img_path, height=200, width=200, fit=f.ImageFit.CONTAIN)

    # Configuration de la barre d'application
    title_img_url = "https://github.com/IroN404/SAE-piloter-un-projet-informatique/blob/main/media/logo_day.png?raw=true"
    page.appbar = f.AppBar(
        leading_width=200,
        title=f.Image(title_img_url, height=95),
        toolbar_height=70,
        center_title=True,
        bgcolor=f.colors.SURFACE_VARIANT,
        actions=[f.IconButton(f.icons.WB_SUNNY_OUTLINED)],
    )

    # Dialogue d'alerte pour tâche vide
    EmptyTaskName = f.AlertDialog(title=f.Text("Entrez un nom pour la tâche"))

    # Gestionnaire d'événements
    def open_dlg(e):
        page.dialog = EmptyTaskName
        EmptyTaskName.open = True
        page.update()

    def add_task(e):
        if not new_task.value:
            open_dlg(e)
        else:
            task_label = f'{new_task.value}  {priority_selector.value}  {tags_selector.value}'
            page.add(f.Checkbox(label=task_label))
            new_task.value = ""
            page.update()

    # Configuration des champs de saisie
    new_task = f.TextField(hint_text="Nouvelle tâche", label='Nom de la tâche', expand=True)
    person = f.TextField(hint_text="Nom de la personne", label='Nom', expand=True)

    priority_options = [
        f.dropdown.Option("Urgent"),
        f.dropdown.Option("Important"),
        f.dropdown.Option("Normal")
    ]
    priority_selector = f.Dropdown(width=200, label="Priorité", hint_text="Niveau de priorité", options=priority_options)

    tag_options = [
        f.dropdown.Option("Travail"),
        f.dropdown.Option("Ecole"),
        f.dropdown.Option("Activitée"),
        f.dropdown.Option("Autre")
    ]
    tags_selector = f.Dropdown(width=200, label="Etiquette", hint_text="Choisissez une étiquette", options=tag_options)

    # Configuration de l'affichage des tâches
    tasks_view = f.Column()

    # Vue principale
    main_view = f.Column(
        width=600,
        controls=[
            f.Row(controls=[new_task]),
            f.Row(controls=[
                person,
                priority_selector,
                tags_selector,
                f.FloatingActionButton(icon=f.icons.ADD, on_click=add_task),
            ]),
            tasks_view,
        ],
    )
    page.horizontal_alignment = f.CrossAxisAlignment.CENTER
    page.add(main_view)

f.app(target=main)
