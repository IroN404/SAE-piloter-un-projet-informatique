# coding:utf-8
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDesktopWidget, QGridLayout, QLabel, QLineEdit, QFormLayout, QComboBox, QTableWidget, QTableWidgetItem, QFrame, QVBoxLayout, QHBoxLayout, QGroupBox, QScrollArea, QSizePolicy, QSpacerItem, QStyle, QStyleOption, QFileDialog, QDialog, QDateEdit, QCheckBox, QProgressBar, QSlider, QDial, QCalendarWidget, QTabWidget, QTabBar, QStackedWidget, QToolButton, QMenu, QMenuBar, QStatusBar, QToolBar, QDockWidget, QStyleFactory, QSystemTrayIcon, QCompleter, QShortcut, QKeySequenceEdit, QSplitter, QInputDialog, QCommandLinkButton, QAbstractItemView, QHeaderView, QStyleOptionViewItem, QStyleOptionTab, QStylePainter, QStyleOptionTabBarBase
from PyQt5.QtCore import Qt, QUrl, QRect, QDate
from pathlib import Path
from PyQt5.QtGui import QIcon, QDesktopServices, QFont
from PyQt5.QtWidgets import QApplication, QFrame, QHBoxLayout, QVBoxLayout, QGridLayout, QWidget
from qfluentwidgets import (CardWidget,NavigationItemPosition, MessageBox, setTheme, Theme, FluentWindow,ImageLabel, CaptionLabel, ElevatedCardWidget,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, InfoBadge,IconWidget, PushButton, TransparentToolButton,
                            BodyLabel, InfoBadgePosition,FluentIcon)
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets.components.widgets.acrylic_label import AcrylicBrush

class AddTaskDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add Task")
        self.setFixedSize(300, 200)
        self.setModal(True)

        self.taskLineEdit = QLineEdit(self)
        self.taskLineEdit.setPlaceholderText("Entrez une tâche...")

        self.priorityComboBox = QComboBox(self)
        self.priorityComboBox.addItems(["Low", "Medium", "High"])
        self.priorityComboBox.setStyleSheet("QComboBox { color: black; }")

        self.personLineEdit = QLineEdit(self)
        self.personLineEdit.setPlaceholderText("Personne en charge...")

        self.addButton = QPushButton("Add", self)
        self.addButton.clicked.connect(self.accept)

        layout = QFormLayout(self)
        layout.addRow("Task Name:", self.taskLineEdit)
        layout.addRow("Priority:", self.priorityComboBox)
        layout.addRow("Person:", self.personLineEdit)
        layout.addRow(self.addButton)

class TaskListWidget(QFrame):
    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)

        self.label = SubtitleLabel(text, self)
        setFont(self.label, 24)
        self.label.setAlignment(Qt.AlignCenter)

        self.addButton = QPushButton("+", self)
        self.addButton.setStyleSheet("""
            QPushButton {
                font-size: 24px;
                color: white;   
                background-color: #0078d7;
                border-radius: 10px;
                border: none;
                width: 40px;
                height: 40px;
                text-align: center;
                item-align: center;
            }
            QPushButton:hover {
                background-color: #0063ad;
            }   
        """)
        self.addButton.setFixedSize(1000, 40)
   
        self.taskTable = QTableWidget(self)
        self.setStyleSheet("""
            
    QTableWidget {
        background-color: white;
        color: black;
    }

    QTableWidget QHeaderView::section {
        background-color: #4DA8DA;
        color: white;
        font-size: 18px;
        height: 40px;
    }

    QTableWidget QTableCornerButton::section {
        background-color: #4DA8DA;
        color: white;
        font-size: 18px;
        height: 40px;
    }

    QTableWidget QScrollBar:vertical {
        background-color: #4DA8DA;
        width: 16px;
    }

    QTableWidget QScrollBar::handle:vertical {
        background-color: #0078D4;
        border: 1px solid #4DA8DA;
        border-radius: 8px;
    }

    QTableWidget QScrollBar::add-line:vertical {
        background-color: #4DA8DA;
        height: 16px;
        subcontrol-position: bottom;
        subcontrol-origin: margin;
    }

    QTableWidget QScrollBar::sub-line:vertical {
        background-color: #4DA8DA;
        height: 16px;
        subcontrol-position: top;
        subcontrol-origin: margin;
    }

    QTableWidget QScrollBar::up-arrow:vertical, QTableWidget QScrollBar::down-arrow:vertical {
        width: 16px;
        height: 16px;
        background-color: #0078D4;
    }

    QTableWidget QScrollBar::add-page:vertical, QTableWidget QScrollBar::sub-page:vertical {
        background-color: #4DA8DA;
    }

    QTableWidget::item:selected {
        background-color: #0078D4;
        color: white;
    }
""")
        self.taskTable.setColumnCount(7)


# ainsi les colonnes prennent toute la place disponible
        header = self.taskTable.horizontalHeader()
        for i in range(7):
            header.setSectionResizeMode(i, QHeaderView.Stretch)
        self.taskTable.setHorizontalHeaderLabels(["Task Name", "Priority", "Person", "Status", "Time Left", "Progress", "Actions"])

        self.taskListLayout = QVBoxLayout(self)
        self.taskListLayout.addWidget(self.label, 1, Qt.AlignLeft)
        self.taskListLayout.addWidget(self.addButton)
        self.taskListLayout.addWidget(self.taskTable)

        self.setObjectName(text.replace(' ', '-'))

        # Connect the button click signal to the showAddTaskDialog method
        self.addButton.clicked.connect(self.showAddTaskDialog)




    def showAddTaskDialog(self):
        dialog = AddTaskDialog(self)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            task_text = dialog.taskLineEdit.text()
            priority = dialog.priorityComboBox.currentText()
            person = dialog.personLineEdit.text()

            if task_text and priority and person != "":
                row_position = self.taskTable.rowCount()
                self.taskTable.insertRow(row_position)

                self.taskTable.setItem(row_position, 0, QTableWidgetItem(task_text))
                self.taskTable.setItem(row_position, 1, QTableWidgetItem(priority))
                self.taskTable.setItem(row_position, 2, QTableWidgetItem(person))
                self.taskTable.setItem(row_position, 3, QTableWidgetItem("To Do"))
                self.taskTable.setItem(row_position, 4, QTableWidgetItem("1 day"))

                # Création et configuration de la barre de progression
                progressBar = QProgressBar()
                progressBar.setMinimum(0)
                progressBar.setMaximum(100)
                progressBar.setValue(0)  # Démarre à 0%
                progressBar.setStyleSheet("""
                    QProgressBar {
                        border: 2px solid grey;
                        border-radius: 1px;
                        text-align: center;
                        background-color: #5DADE2;
                    }

                    QProgressBar::chunk {
                        background-color: #5DADE2;  # Couleur bleutée
                        width: 10px;  # Largeur des chunks de la barre de progression
                    }
                """)

                # Ajout de la barre de progression à la cellule du tableau
                self.taskTable.setCellWidget(row_position, 5, progressBar)

            def updateProgressBar(self, row, value):
                progressBar = self.taskTable.cellWidget(row, 5)
                progressBar.setValue(value)

            # Add a slider to the "Progress" column
            slider = QSlider(Qt.Horizontal, self)
            slider.setStyleSheet("""
                QSlider {
                    background-color: #5DADE2;
                }
                
                QSlider::groove:horizontal {
                    border: 1px solid #bbb;
                    background: white;
                    height: 10px;
                    border-radius: 4px;
                }
                
                QSlider::sub-page:horizontal {
                    background: #5DADE2;
                    border-radius: 4px;
                }
                
                QSlider::add-page:horizontal {
                    background: #5DADE2;
                    border-radius: 4px;
                }
                
                QSlider::handle:horizontal {
                    background: #5DADE2;
                    border: 1px solid #5DADE2;
                    width: 18px;
                    margin-top: -4px;
                    margin-bottom: -4px;
                    border-radius: 4px;
                }
            """)
            # Add Edit and Delete buttons
            delete_button = QPushButton("❌", self)

            # Connect button clicks to corresponding methods
            delete_button.clicked.connect(lambda: self.deleteTask(row_position))

            # Add buttons to the "Actions" column
            self.taskTable.setCellWidget(row_position, 6, delete_button)
            
            

    def editTask(self, row):
        # Add logic for editing task
        pass

    def deleteTask(self, row):
        # Add logic for deleting task
        self.taskTable.removeRow(row)



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
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #4DA8DA, stop: 1 #0078D4);
        border: none;
    }
    
    QCalendarWidget QMenu {
        width: 150px;
        color: white;
        font-size: 18px;
        background-color: #0078D4;
    }
    
    QCalendarWidget QSpinBox {
        width: 150px;
        font-size: 24px;
        color: white;
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #4DA8DA, stop: 1 #0078D4);
        selection-background-color: #003366;
        selection-color: white;
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
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #4DA8DA, stop: 1 #0078D4);
    }
    
    QCalendarWidget QAbstractItemView:enabled {
        font-size: 24px;
        color: #B4B4B4;
        background-color: white;
        selection-background-color: #404040;
        selection-color: #00FF00;
    }
    
    QCalendarWidget QAbstractItemView:disabled {
        color: #404040;
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

        self.setObjectName(text.replace(' ', '-'))

        # Create a main vertical layout
        self.mainLayout = QVBoxLayout(self)

        # Add a subtitle label
        subtitleLabel = SubtitleLabel(text, self)
        setFont(subtitleLabel, 20)
        subtitleLabel.setAlignment(Qt.AlignLeft)
        self.mainLayout.addWidget(subtitleLabel)

        # Add a caption label
        welcomeLabel = CaptionLabel('Bienvenue dans notre application de gestion de tâches !', self)
        self.mainLayout.addWidget(welcomeLabel)

        # Add another caption label
        descriptionLabel = CaptionLabel('Vous pouvez aussi voir les tâches de vos collaborateurs et les modifier si besoin.', self)
        self.mainLayout.addWidget(descriptionLabel)

        # Add the recent task section
        self.mainLayout.addWidget(self.RecentTask())

    def RecentTask(self):
        recentTaskFrame = QFrame(self)

        # Example: Add a label for no recent tasks
        noTaskLabel = QLabel("Aucune tâche récente.", recentTaskFrame)
        noTaskLabel.setAlignment(Qt.AlignCenter)

        # TODO: Add your task-related widgets and layout here

        # Example: Create a layout for centering the message
        layout = QVBoxLayout(recentTaskFrame)
        layout.addWidget(noTaskLabel)

        recentTaskFrame.setLayout(layout)
        return recentTaskFrame


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