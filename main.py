# coding:utf-8
import sys
import sqlite3
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


class DatabaseManager:
    def __init__(self, db_file="tasks.db"):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        query = """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                task_name TEXT,
                priority TEXT,
                person TEXT,
                status TEXT,
                time_left TEXT
            )
        """
        with self.conn:
            self.conn.execute(query)

    def insert_task(self, task_name, priority, person, status, time_left):
        query = "INSERT INTO tasks (task_name, priority, person, status, time_left) VALUES (?, ?, ?, ?, ?)"
        with self.conn:
            self.conn.execute(query, (task_name, priority, person, status, time_left))

    def fetch_all_tasks(self):
        query = "SELECT * FROM tasks"
        with self.conn:
            cursor = self.conn.execute(query)
            return cursor.fetchall()
    
    def delete_task(self, task_id):
        query = "DELETE FROM tasks WHERE id = ?"
        with self.conn:
            self.conn.execute(query, (task_id,))
    
    def fetch_last_task(self):
        query = "SELECT * FROM tasks ORDER BY id DESC LIMIT 1"
        with self.conn:
            cursor = self.conn.execute(query)
            result = cursor.fetchone()

            # Convertir le résultat en un dictionnaire avec des clés appropriées
            if result:
                columns = ["id", "task_name", "priority", "person", "status", "time_left"]
                last_task_dict = dict(zip(columns, result))
                return last_task_dict
            else:
                return None
    
    def get_last_task(db_manager):
        return db_manager.fetch_last_task()


class AddTaskDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Add Task")
        self.setFixedSize(300, 200)
        self.setModal(True)

        self.taskLineEdit = QLineEdit(self)
        self.taskLineEdit.setPlaceholderText("Enter a task...")

        self.priorityComboBox = QComboBox(self)
        self.priorityComboBox.addItems(["Low", "Medium", "High"])
        self.priorityComboBox.setStyleSheet("QComboBox { color: white; }")

        self.personLineEdit = QLineEdit(self)
        self.personLineEdit.setPlaceholderText("Person in charge...")

        # Add the deadline field
        self.deadlineEdit = QDateEdit(self)
        self.deadlineEdit.setCalendarPopup(True)
        self.deadlineEdit.setDate(QDate.currentDate())  # Set the initial date to the current date
        self.deadlineEdit.setDisplayFormat("yyyy-MM-dd")

        self.addButton = QPushButton("Add", self)
        self.addButton.clicked.connect(self.accept)

        layout = QFormLayout(self)
        layout.addRow("Task Name:", self.taskLineEdit)
        layout.addRow("Priority:", self.priorityComboBox)
        layout.addRow("Person:", self.personLineEdit)
        layout.addRow("Deadline:", self.deadlineEdit)
        layout.addRow(self.addButton)

class TaskListWidget(QFrame):
    def __init__(self, text: str, db_manager, parent=None):
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
        self.addButton.setFixedSize(100, 40)
   
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
        self.taskTable.setHorizontalHeaderLabels(["id","Task Name", "Priority", "Person", "Status", "Time Left", "Progress", "Actions"])

        self.taskListLayout = QVBoxLayout(self)
        self.taskListLayout.addWidget(self.label, 1, Qt.AlignLeft)
        self.taskListLayout.addWidget(self.addButton)
        self.taskListLayout.addWidget(self.taskTable)

        self.setObjectName(text.replace(' ', '-'))

        # Add the following line to initialize the db_manager attribute
        self.db_manager = db_manager

        # Connect the button click signal to the showAddTaskDialog method
        self.addButton.clicked.connect(self.showAddTaskDialog)

        # Load tasks from the database when the widget is created
        self.load_tasks_from_database()

        
    def showAddTaskDialog(self):
        dialog = AddTaskDialog(self)
        result = dialog.exec_()

        if result == QDialog.Accepted:
            task_text = dialog.taskLineEdit.text()
            priority = dialog.priorityComboBox.currentText()
            person = dialog.personLineEdit.text()
            deadline = dialog.deadlineEdit.date().toString("yyyy-MM-dd")  # Convert to a string in the format "YYYY-MM-DD"

            if task_text and priority and person != "":
                # Insert the task into the database with the deadline
                self.db_manager.insert_task(task_text, priority, person, "To Do", deadline)

                # Load tasks from the database after inserting a new task
                self.load_tasks_from_database()

    
    def add_task_to_table(self, task_data):
        # Effacez le contenu de la table
        self.taskTable.setRowCount(0)

        # Ajoutez les nouvelles lignes
        for task_data in self.db_manager.fetch_all_tasks():
            row_position = self.taskTable.rowCount()
            self.taskTable.insertRow(row_position)

            # Commencez à ajouter des éléments à partir de la colonne 0
            for col, data in enumerate(task_data):
                item = QTableWidgetItem(str(data))
                self.taskTable.setItem(row_position, col, item)

            # Ajoutez des boutons pour les actions (par exemple, supprimer)
            delete_button = QPushButton("X", self)
            delete_button.setStyleSheet("""
                QPushButton {
                    font-size: 15px;
                    color: red;
                }
            """)  
            delete_button.clicked.connect(lambda _, row=row_position: self.deleteTask(row))
            self.taskTable.setCellWidget(row_position, 6, delete_button)

    def deleteTask(self, row):
        reply = QMessageBox.question(
            self,
            'Confirmation',
            'Êtes-vous sûr de vouloir supprimer cette tâche ?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            # Appel à la méthode delete_task_from_database
            self.delete_task_from_database(row)
    
    def delete_task_from_database(self, row):
        # Récupérez l'ID de la tâche à supprimer
        task_id = self.taskTable.item(row, 0).text()

        # Supprimez la tâche de la base de données
        # Notez que vous devrez peut-être ajuster la méthode delete_task dans DatabaseManager
        self.db_manager.delete_task(task_id)

        # Supprimez la ligne de la table
        self.taskTable.removeRow(row)
    
    # Load tasks from the database when the widget is created
        self.load_tasks_from_database()

    def load_tasks_from_database(self):
        self.taskTable.clearContents()
        tasks = self.db_manager.fetch_all_tasks()
        for task in tasks:
            self.add_task_to_table(task)



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
        pass
    
        

        


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

        # Create an instance of DatabaseManager
        self.db_manager = DatabaseManager()

        # create sub interface
        self.homeInterface = HomeInterface('Home', self)  # Passez db_manager ici
        self.tasklist = TaskListWidget('Task list', self.db_manager, self)
        self.calendar = CalendarWidget('Calendar', self)
        self.settingInterface = Widget('Setting Interface', self)

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