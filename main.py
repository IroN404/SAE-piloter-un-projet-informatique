import sys
from PyQt6.QtWidgets import *

class SimpleUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ToDoList")
        self.setGeometry(200, 300, 1000, 300)  # Définir la taille de la fenêtre

        # Créer un widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Créer une mise en page verticale
        self.layout = QVBoxLayout()
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)
        self.layout.addWidget(exit_button)
        label = QLabel("ToDoList")
        self.layout.addWidget(label)

        self.task_widgets = []  # Pour stocker les widgets de tâche

        # Ajouter des widgets à la mise en page
        plus = QPushButton("+")
        plus.clicked.connect(self.ajoutertache)
        self.layout.addWidget(plus)

        # Définir la mise en page comme mise en page du widget central
        central_widget.setLayout(self.layout)

    def ajoutertache(self):
        label_tache = QLabel("Tâche : ")
        tache = QLineEdit()
        tache.setPlaceholderText("Ajouter une tâche")

        label_statut = QLabel("Statut : ")
        statut = QComboBox()
        statut.setPlaceholderText("Ajouter un statut")
        statut.addItem("En cours")
        statut.addItem("Terminé")
        statut.addItem("En attente")
        self.statut = statut

        label_priorite = QLabel("Priorité : ")
        priorite = QLineEdit()
        priorite.setPlaceholderText("Ajouter une priorité")

        label_personne = QLabel("Personne : ")
        personne = QComboBox()
        personne.setPlaceholderText("Ajouter une personne")
        personne.addItem("Personne 1")
        personne.addItem("Personne 2")
        personne.addItem("Personne 3")
        self.personne = personne

        label_date_debut = QLabel("Date de début : ")
        datedebut = QLineEdit()
        datedebut.setPlaceholderText("Ajouter une date de début")

        label_date_fin = QLabel("Date de fin : ")
        datefin = QLineEdit()
        datefin.setPlaceholderText("Ajouter une date de fin")

        label_date_butoir = QLabel("Date butoir : ")
        date_butoir = QLineEdit()
        date_butoir.setPlaceholderText("Ajouter une date butoir")

        # Ajouter les labels et les champs dans un layout vertical
        inner_layout = QGridLayout()
        inner_layout.addWidget(label_tache, 0, 0)
        inner_layout.addWidget(tache, 1, 0)
        inner_layout.addWidget(label_statut, 0, 1)
        inner_layout.addWidget(statut, 1, 1)
        inner_layout.addWidget(label_priorite, 0, 2)
        inner_layout.addWidget(priorite, 1, 2)
        inner_layout.addWidget(label_personne, 0, 3)
        inner_layout.addWidget(personne, 1, 3)
        inner_layout.addWidget(label_date_debut, 0, 4)
        inner_layout.addWidget(datedebut, 1, 4)
        inner_layout.addWidget(label_date_fin, 0, 5)
        inner_layout.addWidget(datefin, 1, 5)
        inner_layout.addWidget(label_date_butoir, 0, 6)
        inner_layout.addWidget(date_butoir, 1, 6)

        self.layout.addLayout(inner_layout)
        tache.returnPressed.connect(self.pressenter)
        self.task_widgets.append(tache)
        priorite.returnPressed.connect(self.pressenter)
        self.task_widgets.append(priorite)
        datedebut.returnPressed.connect(self.pressenter)
        self.task_widgets.append(datedebut)
        datefin.returnPressed.connect(self.pressenter)
        self.task_widgets.append(datefin)
        date_butoir.returnPressed.connect(self.pressenter)
        self.task_widgets.append(date_butoir)
        statut.activated[int].connect(self.on_combobox_activated)
        self.task_widgets.append(statut)
        personne.activated[int].connect(self.on_combobox_activated2)
        self.task_widgets.append(personne)

    def on_combobox_activated(self, index):
        # index est l'indice de l'élément sélectionné dans le QComboBox
        selected_item = self.statut.itemText(index)

        if selected_item == "En cours":
            # Faites quelque chose lorsque "En cours" est sélectionné
            label = QLabel("En cours")
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()
        elif selected_item == "Terminé":
            # Faites quelque chose lorsque "Terminé" est sélectionné
            label = QLabel("Terminé")
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()
        elif selected_item == "En attente":
            # Faites quelque chose lorsque "En attente" est sélectionné
            label = QLabel("En attente")
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()

    def on_combobox_activated2(self, index):
        # index est l'indice de l'élément sélectionné dans le QComboBox
        selected_item = self.personne.itemText(index)

        if selected_item == "Personne 1":
            # Faites quelque chose lorsque "Personne 1" est sélectionné
            label = QLabel("Personne 1")
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()
        elif selected_item == "Personne 2":
            # Faites quelque chose lorsque "Personne 2" est sélectionné
            label = QLabel("Personne 2")
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()
        elif selected_item == "Personne 3":
            # Faites quelque chose lorsque "Personne 3" est sélectionné
            label = QLabel("Personne 3")
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()

    def pressenter(self):
        if self.sender().text():
            label = QLabel(self.sender().text())
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()
            self.task_widgets.append(label)




def main():
    app = QApplication(sys.argv)
    window = SimpleUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
