import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QVBoxLayout, QDateTimeEdit
from datetime import datetime

class DateSelectionWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sélection de date")

        layout = QVBoxLayout(self)

        self.date_var = QDateTimeEdit(self)
        self.date_var.setCalendarPopup(True)
        self.date_var.setDateTime(datetime.today())
        layout.addWidget(self.date_var)

        self.valider_button = QPushButton("Valider la date", self)
        self.valider_button.clicked.connect(self.valider_date)
        layout.addWidget(self.valider_button)

    def valider_date(self):
        selected_date = self.date_var.dateTime()
        formatted_date = selected_date.toString("dd/MM/yyyy")
        print("Date sélectionnée :", formatted_date)

app = QApplication(sys.argv)
fenetre = QMainWindow()
fenetre.setWindowTitle("Sélection de date")

date_selection_widget = DateSelectionWidget()
fenetre.setCentralWidget(date_selection_widget)

fenetre.resize(320, 380)
fenetre.show()

sys.exit(app.exec())
