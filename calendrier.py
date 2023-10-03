import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QDateTimeEdit
from datetime import datetime

class DateSelectionWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sélection de date et heure")

        layout = QVBoxLayout(self)

        self.date_time_var = QDateTimeEdit(self)
        self.date_time_var.setCalendarPopup(True)
        self.date_time_var.setDateTime(datetime.today())
        layout.addWidget(self.date_time_var)

        self.valider_button = QPushButton("Valider la date et l'heure", self)
        self.valider_button.clicked.connect(self.valider_date)
        layout.addWidget(self.valider_button)

    def valider_date(self):
        selected_date_time = self.date_time_var.dateTime()
        formatted_date_time = selected_date_time.toString("dd/MM/yyyy HH:mm:ss")
        print("Date et heure sélectionnées :", formatted_date_time)

app = QApplication(sys.argv)
fenetre = QMainWindow()
fenetre.setWindowTitle("Sélection de date et heure")

date_selection_widget = DateSelectionWidget()
fenetre.setCentralWidget(date_selection_widget)

fenetre.resize(320, 380)
fenetre.show()

sys.exit(app.exec())
