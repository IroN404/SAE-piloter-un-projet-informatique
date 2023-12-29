# coding:utf-8
import sys

from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, \
    QComboBox, QDateEdit, QPushButton, QCalendarWidget, QLabel
from PyQt5.QtCore import Qt, QUrl, QRect, QDate
from pathlib import Path
from PyQt5.QtGui import QIcon, QDesktopServices, QFont
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QVBoxLayout, QGridLayout, QWidget
from qfluentwidgets import (CardWidget,NavigationItemPosition, MessageBox, setTheme, Theme, FluentWindow,ImageLabel, CaptionLabel, ElevatedCardWidget,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, InfoBadge,IconWidget, PushButton, TransparentToolButton,
                            BodyLabel, InfoBadgePosition,FluentIcon)
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets.components.widgets.acrylic_label import AcrylicBrush

class TaskListWidget(QFrame):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.label = SubtitleLabel(text, self)
        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)

        self.taskLineEdit = QLineEdit(self)
        self.taskLineEdit.setMaxLength(100)
        self.taskLineEdit.setPlaceholderText("Entrez une tâche...")
        self.priorityComboBox = QComboBox(self)
        self.priorityComboBox.addItems(["Low", "Medium", "High"])
        self.priorityComboBox.setStyleSheet("QComboBox { color: balck; }")
        self.personLineEdit = QLineEdit(self)
        self.personLineEdit.setMaxLength(100)
        self.personLineEdit.setPlaceholderText("Personne en charge...")
        self.addButton = QPushButton("Add Task", self)
        self.taskTable = QTableWidget(self)
        self.taskTable.setColumnCount(6)
        self.taskTable.setHorizontalHeaderLabels(["Task Name", "Priority", "Person", "Status","Time Left","Progress"])

        self.taskListLayout = QVBoxLayout(self)
        self.taskListLayout.addWidget(self.label, 1, Qt.AlignLeft)
        self.taskListLayout.addWidget(self.taskLineEdit)
        self.taskListLayout.addWidget(self.priorityComboBox)
        self.taskListLayout.addWidget(self.personLineEdit)
        self.taskListLayout.addWidget(self.addButton)
        self.taskListLayout.addWidget(self.taskTable)

        self.setObjectName(text.replace(' ', '-'))

        # Connect the button click signal to the addTask method
        self.addButton.clicked.connect(self.addTask)

    def addTask(self):
        task_text = self.taskLineEdit.text()
        priority = self.priorityComboBox.currentText()
        person = self.personLineEdit.text()

        if task_text and priority and person != "":
            row_position = self.taskTable.rowCount()
            self.taskTable.insertRow(row_position)

            self.taskTable.setItem(row_position, 0, QTableWidgetItem(task_text))
            self.taskTable.setItem(row_position, 1, QTableWidgetItem(priority))
            self.taskTable.setItem(row_position, 2, QTableWidgetItem(person))
            self.taskTable.setItem(row_position, 3, QTableWidgetItem("To Do"))
            self.taskTable.setItem(row_position, 4, QTableWidgetItem("1 day"))
            self.taskTable.setItem(row_position, 5, QTableWidgetItem("0%"))



            self.taskLineEdit.clear()
            self.priorityComboBox.setCurrentIndex(0)
            self.personLineEdit.clear()




def setFont(widget, size):
    font = QFont("Arial", size)
    widget.setFont(font)

class CalendarWidget(QFrame):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        # Configuration du label
        self.label = SubtitleLabel(text, self)
        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)

        # Création du calendrier
        self.calendar = QCalendarWidget(self)
        self.calendar.setStyleSheet("""
            QCalendarWidget QToolButton {
                height: 60px;
                width: 150px;
                color: white;
                font-size: 24px;
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333);
            }
            QCalendarWidget QMenu {
                width: 150px;
                color: white;
                font-size: 18px;
                background-color: rgb(100, 100, 100);
            }
            QCalendarWidget QSpinBox {
                width: 150px;
                font-size: 24px;
                color: white;
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333);
                selection-background-color: rgb(136, 136, 136);
                selection-color: rgb(255, 255, 255);
            }
            QCalendarWidget QSpinBox::up-button {
                subcontrol-origin: border;
                subcontrol-position: top right;
                width: 65px;
            }
            QCalendarWidget QSpinBox::down-button {
                subcontrol-origin: border;
                subcontrol-position: bottom right;
                width: 65px;
            }
            QCalendarWidget QWidget#qt_calendar_navigationbar {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333);
            }
            QCalendarWidget QAbstractItemView:enabled {
                font-size: 24px;
                color: rgb(180, 180, 180);
                background-color: black;
                selection-background-color: rgb(64, 64, 64);
                selection-color: rgb(0, 255, 0);
            }
            QCalendarWidget QAbstractItemView:disabled {
                color: rgb(64, 64, 64);
            }
        """)

        # Configuration du layout
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label, 1, Qt.AlignCenter)
        self.layout.addWidget(self.calendar, 5)  # Donner plus d'espace au calendrier

        # Définition du nom de l'objet
        self.setObjectName(text.replace(' ', '-'))

class SettingInterface(QFrame):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 20)
        self.label.setAlignment(Qt.AlignLeft)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignLeft)
        self.setObjectName(text.replace('', '-'))


class HomeInterface(QFrame):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 20)
        self.label.setAlignment(Qt.AlignLeft)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace('', '-'))

        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace('', '-'))

        self.label = CaptionLabel('Bienvenue dans notre application de gestion de tâches !', self)
        self.vBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace('', '-'))

        self.label = CaptionLabel('Vous pouvez aussi voir les tâches de vos collaborateurs et les modifier si besoin.', self)
        self.vBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.vBoxLayout.addWidget(self.RecentTask())
        self.setObjectName(text.replace('', '-'))

    def RecentTask(self):
        # Vérifier s'il y a des tâches dans la table
        if self.vBoxLayout.count() == 0:
            # Aucune tâche, afficher un message
            no_task_label = QLabel("Aucune tâche récente.", self)
            no_task_label.setAlignment(Qt.AlignCenter)

            # Créer un layout pour centrer le message
            layout = QVBoxLayout(self)
            layout.addWidget(self.vBoxLayout.label, 1, Qt.AlignCenter)
            layout.addWidget(self.vBoxLayout.taskLineEdit)
            layout.addWidget(self.vBoxLayout.priorityComboBox)
            layout.addWidget(self.vBoxLayout.personLineEdit)
            layout.addWidget(self.vBoxLayout.addButton)
            layout.addWidget(self.vBoxLayout.taskTable)



            layout.addWidget(no_task_label)
            self.setLayout(layout)


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 20)
        self.label.setAlignment(Qt.AlignLeft)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignLeft)
        self.setObjectName(text.replace('', '-'))



class Window(FluentWindow):

    def __init__(self):
        super().__init__()

        # create sub interface
        self.homeInterface = HomeInterface('Home', self)
        self.tasklist = TaskListWidget('Task list', self)
        self.calendar = CalendarWidget('Calendar', self)
        self.settingInterface = Widget('Setting Interface', self)


        # cartes






        self.initNavigation()
        self.initWindow()




    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, 'Home')
        self.addSubInterface(self.tasklist, FIF.CHECKBOX, 'Task list')
        self.addSubInterface(self.calendar, FIF.CALENDAR, 'Calendar')


        self.navigationInterface.addSeparator()


        # self.addSubInterface(self.showMessageBox, FIF.INFO, 'Info')

        # add custom widget to bottom





        self.navigationInterface.addWidget(
            routeKey='avatar',
            widget=NavigationAvatarWidget('Toto', 'media/int.png'),
            onClick=self.showMessageBox,
            position=NavigationItemPosition.BOTTOM,
        )

        self.addSubInterface(self.settingInterface, FIF.SETTING, 'Settings', NavigationItemPosition.BOTTOM)

        # add badge to navigation item
        item = self.navigationInterface.widget(self.calendar.objectName())
        InfoBadge.attension(
            text=9,
            parent=item.parent(),
            target=item,
            position=InfoBadgePosition.NAVIGATION_ITEM
        )

        # NOTE: enable acrylic effect
        # self.navigationInterface.setAcrylicEnabled(True)

    def initWindow(self):
        self.resize(900, 400)
        self.setWindowIcon(QIcon('media/logo_day.png'))
        self.setWindowTitle('To-do list')

        # NOTE: enable acrylic effect



        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

    def showMessageBox(self):
        w = MessageBox(
            '🎉🎉🎉',
            'Bienvenue dans notre to-do list !',
            self

        )
        w.yesButton.setText('Voir le rapport descriptif')
        w.cancelButton.setText('Annuler')



        if w.exec():
            QDesktopServices.openUrl(QUrl("lien du rapport descriptif"))


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)

    # setTheme(Theme.DARK)

    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()