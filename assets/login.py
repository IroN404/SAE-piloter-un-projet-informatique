from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from assets.auth import authenticate # import the authenticate function from auth.py
#from ../widgets.form import FormWidget

class LoginWidget(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget
        self.initUI()

    def initUI(self):
        # Login page properties
        self.setStyleSheet("style/login.css")
        self.setFixedSize(800, 600)

        # Login page widgets
        self.login_title = QLabel("Login")
        self.login_title.setObjectName("login_title")
        self.login_title.setAlignment(Qt.AlignCenter)
        self.login_title.setFixedSize(200, 50)

        self.login_username = QLineEdit()
        self.login_username.setObjectName("login_username")
        self.login_username.setPlaceholderText("Username")
        self.login_username.setFixedSize(200, 50)

        self.login_password = QLineEdit()
        self.login_password.setObjectName("login_password")
        self.login_password.setPlaceholderText("Password")
        self.login_password.setFixedSize(200, 50)
        self.login_password.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.login_button.setObjectName("login_button")
        self.login_button.setFixedSize(200, 50)
        self.login_button.clicked.connect(self.login)

        self.login_signup = QPushButton("Signup")
        self.login_signup.setObjectName("login_signup")
        self.login_signup.setFixedSize(200, 50)
        #self.login_signup.clicked.connect(self.signup)

        # Login page layout
        self.login_layout = QVBoxLayout()
        self.login_layout.setAlignment(Qt.AlignCenter)
        self.login_layout.addWidget(self.login_title)
        self.login_layout.addWidget(self.login_username)
        self.login_layout.addWidget(self.login_password)
        self.login_layout.addWidget(self.login_button)
        self.login_layout.addWidget(self.login_signup)
        self.setLayout(self.login_layout)

    def login(self):
        username = self.login_username.text()
        password = self.login_password.text()
