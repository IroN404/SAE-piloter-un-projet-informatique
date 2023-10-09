import sys
from datetime import datetime
from PyQt6.QtWidgets import QCheckBox, QComboBox, QDateTimeEdit, QLabel, QLineEdit, QPushButton, QMainWindow, QApplication, QWidget, QGridLayout, QScrollArea
from PyQt6 import QtCore as Qt
from PyQt6.QtGui import QPixmap

import subprocess
import os

# Vérifie si le fichier d'indicateur existe
if not os.path.exists("installation.txt"):
    # Exécute le fichier installation.py s'il n'a pas encore été exécuté
    subprocess.run(["python3", "installation.py"])
    # Le reste du code du fichier main.py sera exécuté après l'installation ou si elle a déjà été effectuée.



# Constantes porur les chemins des logos
LOGO_PATHS = {
    "day": "logo_day.png",
    "night": "logo_night.png",
}

STYLES = {
    "day": {
        "canvas": "background-color: white; color: black;",
    },
    "night": {
        "canvas": "background-color: #434343; color: white;",
    },
}



class SimpleUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout = QGridLayout()


        self.setWindowTitle("ToDoList")
        self.setGeometry(200, 300, 1500, 300)  # Définir la taille de la fenêtre

        # Créer un widget central
        central_widget = QWidget()
        central_widget.setStyleSheet("background-color: white;"
                                           "color: black;")


        self.setCentralWidget(central_widget)

        self.layout = QGridLayout()
        self.task_widgets = []  # Pour stocker les widgets de tâche
        self.current_row = 2  # Initialiser la ligne actuelle

        # Ajouter des widgets à la mise en page

        plus = QPushButton("Ajouter une Tache")
        plus.clicked.connect(self.ajoutertache)
        plus.setStyleSheet("border: 1px solid ;")
        self.layout.addWidget(plus, 1, 0, alignment=Qt.Qt.AlignmentFlag.AlignCenter | Qt.Qt.AlignmentFlag.AlignTop)
        # Ligne actuelle, Colonne 3

        # Ajouter une image pour le logo clickable qui change en fonction du mode jour ou nuit
        pixmap = QPixmap('logo_day.png')
        pixmap = pixmap.scaled(310, 150)
        self.logo = QLabel()
        self.logo.setPixmap(pixmap)
        self.logo.mousePressEvent = self.toggle_day_night
        self.layout.addWidget(self.logo, 0, 0, 1, 1, alignment=Qt.Qt.AlignmentFlag.AlignLeft)

        # Définir la mise en page comme mise en page du widget central
        central_widget.setLayout(self.layout)

        # Initialisation du mode actuel (jour ou nuit)
        self.is_night_mode = False

        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setWidget(central_widget)
        self.setCentralWidget(scrollArea)

    def toggle_day_night(self, event):
        # Inversion du mode actuel
        self.is_night_mode = not self.is_night_mode

        # Charger l'image du logo appropriée en fonction du mode jour ou nuit
        logo_path = LOGO_PATHS["night" if self.is_night_mode else "day"]
        pixmap = QPixmap(logo_path)
        pixmap = pixmap.scaled(310, 150)
        self.logo.setPixmap(pixmap)

        # Changer la couleur de fond du widget central de la QScrollArea
        widget = self.centralWidget().widget()
        widget.setStyleSheet(STYLES["night" if self.is_night_mode else "day"]["canvas"])

    def ajoutertache(self):
        # Changement de bouton de place au milieu de la fentre
        self.layout.addWidget(self.sender(), 1, 1, 2, 3 )

        # Incrémenter la ligne actuelle pour ajouter les widgets en dessous
        self.current_row += 2

        # Créer un QLineEdit pour la saisie initiale

        etiquette = QLineEdit()
        etiquette.setPlaceholderText("Ajouter une étiquette")

        tache = QLineEdit()
        tache.setPlaceholderText("Ajouter une tâche")

        label_statut = QLabel("Statut : ")
        statut = QComboBox()
        statut.setPlaceholderText("Ajouter un statut")
        statut.addItem("En cours")
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
        personne = QLineEdit()
        personne.setPlaceholderText("Ajouter une personne")

        label_date_debut = QLabel("Date de début : ")
        datedebut = QDateTimeEdit(self)
        datedebut.setDateTime(datetime.today())
        datedebut.setCalendarPopup(True)
        datedebut.setDisplayFormat("dd/MM/yyyy")

        label_date_butoir = QLabel("Date butoir : ")
        datebutoir = QDateTimeEdit(self)
        datebutoir.setDateTime(datetime.today())
        datebutoir.setCalendarPopup(True)
        datebutoir.setDisplayFormat("dd/MM/yyyy")

        label_tachefinie = QLabel("Tâche finie : ")
        tachefinie = QCheckBox()


        # Ajouter les labels et les champs dans un layout vertical

        self.layout.addWidget(etiquette, self.current_row, 0)
        self.layout.addWidget(tache, self.current_row + 1, 0)
        self.layout.addWidget(label_statut, self.current_row, 1)
        self.layout.addWidget(statut, self.current_row + 1, 1)
        self.layout.addWidget(label_priorite, self.current_row, 2)
        self.layout.addWidget(priorite, self.current_row + 1, 2)
        self.layout.addWidget(label_personne, self.current_row, 3)
        self.layout.addWidget(personne, self.current_row + 1, 3)
        self.layout.addWidget(label_date_debut, self.current_row, 4)
        self.layout.addWidget(datedebut, self.current_row + 1, 4)
        self.layout.addWidget(label_date_butoir, self.current_row, 5)
        self.layout.addWidget(datebutoir, self.current_row + 1, 5)
        self.layout.addWidget(label_tachefinie, self.current_row, 6)
        self.layout.addWidget(tachefinie, self.current_row + 1, 6)

        # Mettre tous les champs en forme de tableau pour qu'ils soient alignés sur css

        etiquette.returnPressed.connect(self.pressenteretiquette)
        tache.returnPressed.connect(self.pressenter)
        self.task_widgets.append(tache)
        priorite.activated[int].connect(self.on_combobox_activated3)
        self.task_widgets.append(priorite)
        datedebut.dateTimeChanged.connect(self.pressenter)
        self.task_widgets.append(datedebut)
        datebutoir.dateTimeChanged.connect(self.pressenter)
        self.task_widgets.append(datebutoir)
        statut.activated[int].connect(self.on_combobox_activated)
        self.task_widgets.append(statut)
        personne.returnPressed.connect(self.pressenter)
        self.task_widgets.append(personne)
        tachefinie.stateChanged.connect(self.checkbox1)
        self.task_widgets.append(tachefinie)

    def on_combobox_activated(self, index):
        # index est l'indice de l'élément sélectionné dans le QComboBox
        selected_item = self.statut.itemText(index)

        if selected_item == "En cours":
            # Faites quelque chose lorsque "En cours" est sélectionné
            label = QLabel("En cours")
            label.setStyleSheet("border: 1px solid;background-color: blue;")
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()

        elif selected_item == "En attente":
            # Faites quelque chose lorsque "En attente" est sélectionné
            label = QLabel("En attente")
            label.setStyleSheet("border: 1px solid;background-color: vert;")
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()

    def on_combobox_activated3(self, index):
        # index est l'indice de l'élément sélectionné dans le QComboBox
        selected_item = self.priorite.itemText(index)

        if selected_item == "P1":
            # Faites quelque chose lorsque "P1" est sélectionné
            label = QLabel("P1")
            label.setStyleSheet("border: 1px solid;background-color: red;")  # Changer la couleur en rouge
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()

        elif selected_item == "P2":
            # Faites quelque chose lorsque "P2" est sélectionné
            label = QLabel("P2")
            label.setStyleSheet("border: 1px solid;background-color: orange;")  # Changer la couleur en orange
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()

        elif selected_item == "P3":
            # Faites quelque chose lorsque "P3" est sélectionné
            label = QLabel("P3")
            label.setStyleSheet("border: 1px solid;background-color: yellow;")  # Changer la couleur en jaune
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()

    def pressenter(self):
        if self.sender().text():
            label = QLabel(self.sender().text())
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()
            self.task_widgets.append(label)

    def pressenteretiquette(self):
        if self.sender().text():
            label = QLabel(self.sender().text())
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()
            self.task_widgets.append(label)

    def checkbox1(self):
        labledatedefin = QLabel(datetime.now().strftime("%d-%m-%Y %H:%M"))
        self.layout.replaceWidget(self.sender(), labledatedefin)
        self.sender().deleteLater()
        self.task_widgets.append(labledatedefin)

def main():
    app = QApplication(sys.argv)
    window = SimpleUI()
    window.showMaximized()
    window.show()
    window.showMaximized()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
