import sys
from PyQt6.QtWidgets import *


class SimpleUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ToDoList")
        self.setGeometry(200, 300, 1500, 300)  # Définir la taille de la fenêtre

        # Créer un widget central
        central_widget = QWidget()
        central_widget.setStyleSheet("""
            QWidget {
                background-color: grey;
            }
            """)
        self.setCentralWidget(central_widget)

        # Créer une mise en page verticale
        self.layout = QGridLayout()
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)
        self.layout.addWidget(exit_button, 0, 3)  # Ligne 0, Colonne 3
        exit_button.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 5px;
                color: black;
                font-size: 16px;
            }
            """)
        label = QLabel("ToDoList")
        self.layout.addWidget(label, 1, 3)  # Ligne 1, Colonne 3

        self.task_widgets = []  # Pour stocker les widgets de tâche
        self.current_row = 2  # Initialiser la ligne actuelle

        # Ajouter des widgets à la mise en page
        plus = QPushButton("+")
        plus.clicked.connect(self.ajoutertache)
        self.layout.addWidget(plus, self.current_row, 3)  # Ligne actuelle, Colonne 3
        plus.setStyleSheet("""
            QPushButton {
                background-color: white;
                border-radius: 5px;
                color: black;
                font-size: 16px;
            }
            """)


        # Définir la mise en page comme mise en page du widget central
        central_widget.setLayout(self.layout)

    def ajoutertache(self):
        # Incrémenter la ligne actuelle pour ajouter les widgets en dessous
        self.current_row += 2

        # Créer un QLineEdit pour la saisie initiale

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
        priorite = QComboBox()
        priorite.setPlaceholderText("Ajouter une priorité")
        priorite.addItem("P1")
        priorite.addItem("P2")
        priorite.addItem("P3")
        self.priorite = priorite

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

        label_tachefinie = QLabel("Tâche finie : ")
        tachefinie = QCheckBox()

        # Ajouter les labels et les champs dans un layout vertical

        self.layout.addWidget(tache, self.current_row + 1, 0)
        self.layout.addWidget(label_statut, self.current_row, 1)
        self.layout.addWidget(statut, self.current_row + 1, 1)
        self.layout.addWidget(label_priorite, self.current_row, 2)
        self.layout.addWidget(priorite, self.current_row + 1, 2)
        self.layout.addWidget(label_personne, self.current_row, 3)
        self.layout.addWidget(personne, self.current_row + 1, 3)
        self.layout.addWidget(label_date_debut, self.current_row, 4)
        self.layout.addWidget(datedebut, self.current_row + 1, 4)
        self.layout.addWidget(label_date_fin, self.current_row, 5)
        self.layout.addWidget(datefin, self.current_row + 1, 5)
        self.layout.addWidget(label_date_butoir, self.current_row, 6)
        self.layout.addWidget(date_butoir, self.current_row + 1, 6)
        self.layout.addWidget(label_tachefinie, self.current_row, 7)
        self.layout.addWidget(tachefinie, self.current_row + 1, 7)

        # Mettre tous les champs en forme de tableau pour qu'ils soient alignés sur css




        tache.returnPressed.connect(self.pressenter)
        self.task_widgets.append(tache)
        priorite.activated[int].connect(self.on_combobox_activated3)
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

    def on_combobox_activated3(self, index):
        # index est l'indice de l'élément sélectionné dans le QComboBox
        selected_item = self.priorite.itemText(index)

        if selected_item == "P1":
            # Faites quelque chose lorsque "P1" est sélectionné
            label = QLabel("P1")
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()
        elif selected_item == "P2":
            # Faites quelque chose lorsque "P2" est sélectionné
            label = QLabel("P2")
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()
        elif selected_item == "P3":
            # Faites quelque chose lorsque "P3" est sélectionné
            label = QLabel("P3")
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
