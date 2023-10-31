from PyQt5.QtWidgets import *
import sys

#from assets.login import LoginWidget
#from assets.landing import LandingWidget
#from assets.signup import SignupWidget

def initUI(main_window):
    # Main window properties
    main_window.setWindowTitle("GUI-todo-app") # titre de la fenetre
    main_window.setContentsMargins(0, 0, 0, 0) # remove margins
    main_window.setFixedSize(800, 600) # window's size
    main_window.setStyleSheet("style/main_window.css") # window's style

def StackeWidget(main_window):
    # QstackedWidget creation
    stacked_widget = QStackedWidget()
    main_window.setCentralWidget(stacked_widget)

    # Listing all pages of the app
    #login_page = LoginWidget(stacked_widget)
    #landing_page = LandingWidget(stacked_widget)
    #signup_page = SignupWidget(stacked_widget)

    # Adding pages to the QStackedWidget
    #stacked_widget.addWidget(login_page)
    #stacked_widget.addWidget(landing_page)
    #stacked_widget.addWidget(signup_page)

    # Displaying the login page
    #stacked_widget.setCurrentWidget(login_page)

def main():
    app = QApplication([])

    main_window = QMainWindow()
    initUI(main_window)
    StackeWidget(main_window)

    # Starting the app
    main_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()