import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, pyqtSignal
from PIL import Image
from PIL.ImageQt import ImageQt

# Largeur du logo
LOGO_WIDTH = 150

# Constantes pour les chemins des logos
LOGO_PATHS = {
    "day": "logo_day.png",
    "night": "logo_night.png",
}

# Styles pour le mode jour et nuit
STYLES = {
    "day": {
        "canvas": "background-color: white;",
        "label": "color: black; background-color: transparent;",
    },
    "night": {
        "canvas": "background-color: grey;",
        "label": "color: white; background-color: grey;",
    },
}

# Classe pour créer un QLabel cliquable
class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()

# Classe pour le QLabel qui affiche le logo
class LogoLabel(ClickableLabel):
    def load_image(self, filename):
        # Ouvrir l'image et la redimensionner
        image = Image.open(filename)
        image = image.resize((LOGO_WIDTH, LOGO_WIDTH), Image.ANTIALIAS)
        # Afficher l'image dans le QLabel
        self.setPixmap(QPixmap.fromImage(ImageQt(image)))

# Classe principale de l'application
class ModeJourNuitApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Configuration de la fenêtre principale
        self.setWindowTitle("Mode Jour/Nuit")
        self.setGeometry(100, 100, 300, 300)

        # Création du widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Création du layout principal
        self.main_layout = QVBoxLayout(self.central_widget)

        # Création d'un canevas pour afficher le logo
        self.canvas = QWidget()
        self.canvas_layout = QVBoxLayout(self.canvas)

        # Charger le logo initial pour le mode jour
        self.day_logo = LogoLabel()
        self.day_logo.load_image(LOGO_PATHS["day"])
        self.canvas_layout.addWidget(self.day_logo)

        self.main_layout.addWidget(self.canvas)

        # Création d'un QLabel pour afficher du texte
        self.label = QLabel("Cliquez sur le logo pour basculer entre le mode jour et nuit")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.label)

        # Initialisation du mode actuel (jour ou nuit)
        self.is_night_mode = False

        # Connexion du signal "clicked" du logo jour à la méthode toggle_day_night()
        self.day_logo.clicked.connect(self.toggle_day_night)

    def toggle_day_night(self):
        # Inversion du mode actuel
        self.is_night_mode = not self.is_night_mode

        # Appliquer le mode jour ou nuit en fonction de l'état actuel
        if self.is_night_mode:
            self.set_night_mode()
        else:
            self.set_day_mode()

    def set_day_mode(self):
        # Appliquer les styles et charger le logo pour le mode jour
        self.canvas.setStyleSheet(STYLES["day"]["canvas"])
        self.label.setStyleSheet(STYLES["day"]["label"])
        self.day_logo.load_image(LOGO_PATHS["day"])

    def set_night_mode(self):
        # Appliquer les styles et charger le logo pour le mode nuit
        self.canvas.setStyleSheet(STYLES["night"]["canvas"])
        self.label.setStyleSheet(STYLES["night"]["label"])
        self.day_logo.load_image(LOGO_PATHS["night"])

# Fonction principale pour exécuter l'application
def main():
    app = QApplication(sys.argv)
    main_window = ModeJourNuitApp()
    main_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
