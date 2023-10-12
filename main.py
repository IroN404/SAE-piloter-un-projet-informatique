import flet as f


def main(page: f.Page):

    page.theme_mode = "light"

    def changetheme(e):
        page.theme_mode = "light" if page.theme_mode == "dark" else "dark"
        page.update()

        toggledarklight.selected = not toggledarklight.selected

        if page.theme_mode == "light":
            page.appbar.title = f.Image(
                "https://github.com/IroN404/SAE-piloter-un-projet-informatique/blob/main/media/logo_day.png?raw=true",
                height=75)
        else:
            page.appbar.title = f.Image(
                "https://github.com/IroN404/SAE-piloter-un-projet-informatique/blob/main/media/logo_night.png?raw=true",
                height=75)

        page.update()

    toggledarklight = f.IconButton(
        on_click=changetheme,
        icon="dark_mode",
        selected_icon="light_mode",
        style=f.ButtonStyle(
            color={"": f.colors.BLACK, "selected": f.colors.WHITE}
        )
    )


    # Configuration de l'AppBar avec le bouton inclus
    page.appbar = f.AppBar(
        toolbar_height=0,
        title=f.Image("https://github.com/IroN404/SAE-piloter-un-projet-informatique/blob/main/media/logo_day.png?raw=true", height=75),
        center_title=True,
        actions=[
            toggledarklight
        ]
    )


    EmptyTaskName = f.AlertDialog(title=f.Text("Entrez un nom pour la tâche"))

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

    tasks_view = f.Column()

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
