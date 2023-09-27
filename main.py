import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

class SimpleUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ToDoList")
        self.setGeometry(100, 100, 400, 200)  # Définir la taille de la fenêtre

        # Créer un widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Créer une mise en page verticale
        layout = QVBoxLayout()

        # Ajouter des widgets à la mise en page
        label = QLabel("Ceci est une étiquette.")
        exit = QPushButton("Exit")
        exit.clicked.connect(self.close)

        layout.addWidget(label)
        layout.addWidget(exit)

        # Définir la mise en page comme mise en page du widget central
        central_widget.setLayout(layout)

def main():
    app = QApplication(sys.argv)
    window = SimpleUI()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
