# coding:utf-8
import sys

from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QComboBox, QDateEdit, QPushButton
from PyQt5.QtCore import Qt, QUrl
from pathlib import Path
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QVBoxLayout
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
        self.priorityComboBox = QComboBox(self)
        self.priorityComboBox.addItems(["Low", "Medium", "High"])
        self.priorityComboBox.setStyleSheet("QComboBox { color: balck; }")
        self.personLineEdit = QLineEdit(self)
        self.addButton = QPushButton("Add Task", self)
        self.taskTable = QTableWidget(self)
        self.taskTable.setColumnCount(4)
        self.taskTable.setHorizontalHeaderLabels(["Task", "Priority", "Person"])

        self.taskListLayout = QVBoxLayout(self)
        self.taskListLayout.addWidget(self.label, 1, Qt.AlignCenter)
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

            self.taskLineEdit.clear()
            self.priorityComboBox.setCurrentIndex(0)
            self.personLineEdit.clear()

class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 1, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))




class Window(FluentWindow):

    def __init__(self):
        super().__init__()

        # create sub interface
        self.homeInterface = Widget('Home', self)
        self.tasklist = TaskListWidget('Task list', self)
        self.calendar = Widget('Calendar', self)
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
        self.resize(900, 700)
        self.setWindowIcon(QIcon('media/logo_day.png'))
        self.setWindowTitle('To-do list')



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