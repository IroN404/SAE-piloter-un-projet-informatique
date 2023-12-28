# coding:utf-8
import sys

from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, \
    QComboBox, QDateEdit, QPushButton
from PyQt5.QtCore import Qt, QUrl
from pathlib import Path
from PyQt5.QtGui import QIcon, QDesktopServices
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QVBoxLayout, QGridLayout, QWidget
from qfluentwidgets import (CardWidget, NavigationItemPosition, MessageBox, setTheme, Theme, FluentWindow, ImageLabel,
                            CaptionLabel, ElevatedCardWidget,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, InfoBadge, IconWidget, PushButton,
                            TransparentToolButton,
                            BodyLabel, InfoBadgePosition, FluentIcon)
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
        self.priorityComboBox.setStyleSheet("QComboBox { color: black; }")
        self.personLineEdit = QLineEdit(self)
        self.personLineEdit.setMaxLength(100)
        self.personLineEdit.setPlaceholderText("Personne en charge...")
        self.addButton = QPushButton("Add Task", self)
        self.taskTable = QTableWidget(self)
        self.taskTable.setColumnCount(6)
        self.taskTable.setHorizontalHeaderLabels(["Task Name", "Priority", "Person", "Status", "Time Left", "Progress"])

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
            self.taskTable.setItem(row_position, 3, QTableWidgetItem("To Do"))
            self.taskTable.setItem(row_position, 4, QTableWidgetItem("1 day"))
            self.taskTable.setItem(row_position, 5, QTableWidgetItem("0%"))

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
        self.gridgrid = QGridLayout()
        self.widget = QWidget()
        self.widget.setLayout(self.gridgrid)
        self.widget.setObjectName("widget")
        self.widget.setStyleSheet("QWidget#widget{background: red}")
        self.gridgrid.setContentsMargins(0, 0, 0, 0)
        self.gridgrid.setSpacing(0)
        self.gridgrid.setObjectName("gridLayout_2")
        self.gridgrid.addWidget(self.homeInterface, 0, 0, 1, 1)
        self.gridgrid.addWidget(self.tasklist, 0, 1, 1, 1)
        self.gridgrid.addWidget(self.calendar, 0, 2, 1, 1)
        self.gridgrid.addWidget(self.settingInterface, 0, 3, 1, 1)
        self.gridgrid.addWidget(self.widget, 1, 0, 1, 4)
        self.gridgrid.setColumnStretch(0, 1)
        self.gridgrid.setColumnStretch(1, 1)

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

        # NOTE: enable acrylic effect

        desktop = QApplication.desktop().availableGeometry()
        message, h = desktop.width(), desktop.height()
        self.move(message // 2 - self.width() // 2, h // 2 - self.height() // 2)

    def showMessageBox(self):
        message = MessageBox(
            '🎉🎉🎉',
            'Bienvenue dans notre to-do list !',
            self

        )
        message.yesButton.setText('Voir le rapport descriptif')
        message.cancelButton.setText('Annuler')

        if message.exec():
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
