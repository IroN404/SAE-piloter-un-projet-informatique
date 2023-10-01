import sys
from PyQt6.QtWidgets import *
from PyQt6 import QtCore as Qt
import datetime


class SimpleUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ToDoList")
        self.setGeometry(200, 300, 1500, 300)  # Définir la taille de la fenêtre

        # Créer un widget central
        central_widget = QWidget()
        central_widget.setStyleSheet("""
            QWidget {
                background-color: white;
                color: black;
                margin: 0px;
                padding: 0px;
            }
            """)
        self.setCentralWidget(central_widget)

        label = QLabel("ToDoList")
        label.setStyleSheet("""
            QLabel {
                background-color: grey;
                border-radius: 5px;
                border: 3px solid black;
                color: white;
                text-align: center;
                font-size: 16px;
                padding: 5px;
                margin: 0px;
            }
            """)
        self.layout = QGridLayout()
        self.layout.addWidget(label, 0, 0, 1, 8)  # Ligne 0, Colonne 0, 1 ligne, 8 colonnes

        # Créer une mise en page verticale
        """
        self.layout = QGridLayout()
        exit_button = QPushButton("Exit")
        exit_button.clicked.connect(self.close)
        self.layout.addWidget(exit_button, 0, 3)  # Ligne 0, Colonne 3
        exit_button.setStyleSheet(
            
        label = QLabel("ToDoList")
        self.layout.addWidget(label, 1, 3)  # Ligne 1, Colonne 3
        """

        self.task_widgets = []  # Pour stocker les widgets de tâche
        self.current_row = 2  # Initialiser la ligne actuelle

        # Ajouter des widgets à la mise en page
        plus = QPushButton("+")
        plus.clicked.connect(self.ajoutertache)
        self.layout.addWidget(plus, self.current_row, 3)  # Ligne actuelle, Colonne 3
        plus.setStyleSheet("""
            QPushButton {
                background-color: black;
                border-radius: 5px;
                color: white;
                font-size: 16px;
            }
            """)


        # Définir la mise en page comme mise en page du widget central
        central_widget.setLayout(self.layout)

    def ajoutertache(self):
        # Incrémenter la ligne actuelle pour ajouter les widgets en dessous
        self.current_row += 2

        # Créer un QLineEdit pour la saisie initiale

        etiquette = QLineEdit()
        etiquette.setPlaceholderText("Ajouter une étiquette")
        etiquette.setStyleSheet("""
            QLineEdit {
                width: 20px;
                background-color: white;
                border-radius: 2px;
                color: black;
                font-size: 10px;
                padding: 5px;
                margin: 0px;
            }
            """)
        tache = QLineEdit()
        tache.setPlaceholderText("Ajouter une tâche")

        label_statut = QLabel("Statut : ")
        statut = QComboBox()
        statut.setPlaceholderText("Ajouter un statut")
        statut.addItem("En cours")
        """statut.addItem("Terminé")"""
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

        label_date_fin = QLabel("Date de fin réel: ")
        datefin = QLabel()

        label_date_butoir = QLabel("Date butoir : ")
        date_butoir = QLineEdit()
        date_butoir.setPlaceholderText("Ajouter une date butoir")



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
        self.layout.addWidget(label_date_fin, self.current_row, 5)
        self.layout.addWidget(datefin, self.current_row + 1, 5)
        self.layout.addWidget(label_date_butoir, self.current_row, 6)
        self.layout.addWidget(date_butoir, self.current_row + 1, 6)


        # Mettre tous les champs en forme de tableau pour qu'ils soient alignés sur css



        etiquette.returnPressed.connect(self.pressenteretiquette)
        tache.returnPressed.connect(self.pressenter)
        self.task_widgets.append(tache)
        priorite.activated[int].connect(self.on_combobox_activated3)
        self.task_widgets.append(priorite)
        datedebut.returnPressed.connect(self.pressenter)
        self.task_widgets.append(datedebut)
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
            label.setStyleSheet("""
                QLabel {
                    background-color: blue;
                    border-radius: 5px;
                    color: white;
                    font-size: 16px;
                    padding: 5px;
                }
                """)

            label_tachefinie = QLabel("Tâche finie : ")
            tachefinie = QCheckBox()
            self.layout.addWidget(label_tachefinie, self.current_row, 7)
            self.layout.addWidget(tachefinie, self.current_row + 1, 7)
            tachefinie.stateChanged.connect(self.checkbox1)
            self.task_widgets.append(tachefinie)



        elif selected_item == "En attente":
            # Faites quelque chose lorsque "En attente" est sélectionné
            label = QLabel("En attente")
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()
            label.setStyleSheet("""
                QLabel {
                    background-color: #a319ff;
                    border-radius: 5px;
                    color: white;
                    font-size: 16px;
                    padding: 5px;
                }
                """)



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
            label.setStyleSheet("""
                QLabel {
                    background-color: red;
                    border-radius: 5px;
                    color: white;
                    font-size: 16px;
                    padding: 5px;
                }
                """)
        elif selected_item == "P2":
            # Faites quelque chose lorsque "P2" est sélectionné
            label = QLabel("P2")
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()
            label.setStyleSheet("""
                QLabel {
                    background-color: orange;
                    border-radius: 5px;
                    color: white;
                    font-size: 16px;
                    padding: 5px;
                }
                """)
        elif selected_item == "P3":
            # Faites quelque chose lorsque "P3" est sélectionné
            label = QLabel("P3")
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()
            label.setStyleSheet("""
                QLabel {
                    background-color: #ffc400;
                    border-radius: 5px;
                    color: white;
                    font-size: 16px;
                    padding: 5px;
                }
                """)

    def pressenter(self):
        if self.sender().text():
            label = QLabel(self.sender().text())
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()
            self.task_widgets.append(label)
            label.setStyleSheet("""
                QLabel {
                    background-color: white;
                    border-radius: 
                    2px;
                    border: 3px solid grey;
                    color: black;
                    font-size: 16px;
                    padding: 5px;
                    margin: 0px;
                }
                """)



    def pressenteretiquette(self):
        if self.sender().text():
            label = QLabel(self.sender().text())
            self.layout.replaceWidget(self.sender(), label)
            self.sender().deleteLater()
            self.task_widgets.append(label)
            label.setStyleSheet("""
                QLabel {
                    color: black;
                    font-size: 10px;
                }
                """)

    def checkbox1(self):
        labledatedefin = QLabel(datetime.datetime.now().strftime("%d-%m-%Y %H:%M"))
        self.layout.addWidget(labledatedefin, self.current_row + 1, 5)
        labledatedefin.setStyleSheet("""
                                QLabel {
                                    background-color: white;
                                    border-radius: 2px;
                                    color: black;
                                    font-size: 16px;
                                    padding: 5px;
                                    margin: 0px;
                                }
                                """)
        statut = QLabel("Terminé")
        self.layout.addWidget(statut, self.current_row + 1, 1)
        statut.setStyleSheet("""
                                QLabel {
                                    background-color: green;
                                    color: white;
                                    font-size: 20px;
                                    padding: 5px;

                                }
                                """)



def main():
    app = QApplication(sys.argv)
    window = SimpleUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
