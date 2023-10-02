import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, pyqtSignal
from PIL import Image
from PIL.ImageQt import ImageQt

class ClickableLabel(QLabel):
    clicked = pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()

class ModeJourNuitApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Mode Jour/Nuit")
        self.setGeometry(100, 100, 300, 300)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        # Créez un canevas pour afficher le logo
        self.canvas = QWidget()
        self.canvas.setStyleSheet("background-color: white;")
        self.canvas_layout = QVBoxLayout()
        self.canvas.setLayout(self.canvas_layout)

        # Chargez le logo initial pour le mode jour
        self.day_image = Image.open("logo_day.png")
        self.day_image = self.day_image.resize((150, 150), Image.ANTIALIAS)
        self.day_image = ImageQt(self.day_image)
        self.day_pixmap = QPixmap.fromImage(self.day_image)
        self.day_label = ClickableLabel()
        self.day_label.setPixmap(self.day_pixmap)
        self.day_label.clicked.connect(self.toggle_day_night)
        self.canvas_layout.addWidget(self.day_label)

        self.main_layout.addWidget(self.canvas)

        # Créez un label pour afficher du texte
        self.label = QLabel("Cliquez sur le logo pour basculer entre le mode jour et nuit")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.label)

        # Définissez une variable pour suivre le mode actuel (jour ou nuit)
        self.is_night_mode = False

    def toggle_day_night(self):
        if self.is_night_mode:
            # Passage en mode jour
            self.canvas.setStyleSheet("background-color: white;")
            self.label.setStyleSheet("color: black; background-color: transparent;")
            self.day_label.setPixmap(self.day_pixmap)
            self.is_night_mode = False
        else:
            # Passage en mode nuit
            self.canvas.setStyleSheet("background-color: grey;")
            self.label.setStyleSheet("color: white; background-color: grey;")
            # Chargez le logo de nuit (remplacez "logo_night.png" par le chemin de votre image de nuit)
            night_image = Image.open("logo_night.png")
            night_image = night_image.resize((150, 150), Image.ANTIALIAS)
            self.night_image = ImageQt(night_image)
            self.night_pixmap = QPixmap.fromImage(self.night_image)
            self.day_label.setPixmap(self.night_pixmap)
            self.is_night_mode = True

def main():
    app = QApplication(sys.argv)
    mainWindow = ModeJourNuitApp()
    mainWindow.show()
    app.exec()

if __name__ == "__main__":
    main()
