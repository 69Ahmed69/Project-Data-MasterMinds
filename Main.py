import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QMessageBox, QWidget, QLineEdit
from PyQt6.uic.load_ui import loadUi
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import pyqtSignal, QTimer
from User import User 
import os
class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        current_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(current_dir, "icon.png")
        self.setWindowTitle("AcademIQ")
        self.setWindowIcon(QIcon(icon_path))
        current_dir = os.path.dirname(os.path.abspath(__file__))
        stylesheet_path = os.path.join(current_dir, "QSS-master", "MaterialDark.qss")
        self.loadStylesheet(stylesheet_path)
        self.welcome = WelcomeScreen(self)
        self.setCentralWidget(self.welcome)
        self.username = ''
        self.access_right = 0
        QTimer.singleShot(4000, self.showLogin)

    def loadStylesheet(self, path):
        try:
            with open(path, "r") as f:
                stylesheet = f.read()
            self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"Error: Stylesheet file not found at {path}")
        
    def showLogin(self):
        self.login_ui = LoginUi(self)
        self.login_ui.login_successful.connect(self.loadApp)
        self.setCentralWidget(self.login_ui)

    def loadApp(self, username, access):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file_path = os.path.join(current_dir, "Main.ui")
        self.load_ui(ui_file_path)
        self.access = access
        self.lockAccess()
        self.setupTabWidget()
        self.updateUserInfo(username, access)
        self.connectSignals()

    def load_ui(self, path):
        try:
            loadUi(path, self)
        except FileNotFoundError:
            print(f"Error: UI file not found at {path}")

    def setupTabWidget(self):
        self.tabWidget.tabBar().setVisible(False)
        self.tabWidget.setCurrentIndex(0)

    def updateUserInfo(self, username, access):
        self.current_user.setText(f"User: <font color='green'>{username}</font>")
        self.access_right.setText(f"Access Right: <font color='green'>{access}</font>")

    def connectSignals(self):
        self.new_user_button.clicked.connect(self.AddNewUser)
        self.delete_user_button.clicked.connect(self.handleDelete)
        self.modify_button.clicked.connect(self.handleModify)
        self.modify_button_2.clicked.connect(self.modifyUser)
        self.change_password_button.clicked.connect(self.handleChangePassword)
        self.show_button.clicked.connect(self.passwordModeChange)
        self.actionLight_Mode.triggered.connect(self.changeThemeLight)
        self.actionAqua_Mode.triggered.connect(self.changeThemeAqua)
        self.actionDark_Mode.triggered.connect(self.changeThemeDark)
        self.actionConsole_Mode.triggered.connect(self.changeThemeConsole)
        
    def lockAccess(self):
        if self.access < 4:
            self.delete_user_button.setEnabled(False)
            self.modify_button.setEnabled(False)
            self.new_user_button.setEnabled(False)
            
            
    def AddNewUser(self):
        self.tabWidget.setCurrentIndex(1)
        self.register_button.clicked.connect(self.RegisterUser)
        
    def handleDelete(self):
        self.tabWidget.setCurrentIndex(2)
        self.delete_user_button_2.clicked.connect(self.deleteUser)
        
    def handleModify(self):
        self.tabWidget.setCurrentIndex(3)
        self.search_user_button.clicked.connect(self.searchUser)
        
    def handleChangePassword(self):
        self.tabWidget.setCurrentIndex(4)
        self.change_password_button_2.clicked.connect(self.changePassword)
        
    def RegisterUser(self):
        username = self.username_read.text() 
        if username != "":
            password = self.password_read.text()
            password2 = self.password2_read.text()
            if password != "" and password2 != "":
                if password == password2:
                    access_right = self.access_right_read.currentText()
                    access_right = int(access_right[0])
                    User.register_user(username, password, access_right)
                    QMessageBox.information(self, 'Registration Successful', f'User {username} was successfully registered')
                    self.username_read.clear()
                    self.password_read.clear()
                    self.password2_read.clear()
                else:
                    QMessageBox.warning(self, 'Password mismatch', 'Please make sure that your passwords match.')
            else:
                QMessageBox.warning(self, 'Blank Password', 'Please enter a valid password.')
        else:
            QMessageBox.warning(self, 'Blank input', 'Please enter a valid Username.')
        
    def deleteUser(self):
        username = self.user_delete_read.text() 
        if username != "":
            exists = User.user_exists(username)
            if exists:
                reply = QMessageBox.question(self, "Confirmation", "Are you sure you want to delete?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
                if reply == QMessageBox.StandardButton.Yes:
                    User.delete_user(username)
                    QMessageBox.information(None, 'User deleted', f'The user {username} has been deleted successfully.')
                    self.user_delete_read.clear()
            else:
                QMessageBox.warning(self, 'User not found', 'The specified user does not exist.')
        else:
            QMessageBox.warning(self, 'Blank input', 'Please enter a valid Username.')
            
    def searchUser(self):
        username = self.search_user_read.text()
        if username != "":
            exists = User.user_exists(username)
            if exists:
                access = User.get_access_right(username)
                self.username = username
                self.access = access
                self.access_label.setText(f'Current access right: {access}')
                self.new_user_read.setEnabled(True)
                self.access_right_read_3.setEnabled(True)
                self.modify_button_2.setEnabled(True)
            else:
                QMessageBox.warning(self, 'User not found', 'The specified user does not exist.')
        else:
            QMessageBox.warning(self, 'Blank input', 'Please enter a valid Username.')
            
    def modifyUser(self):
        username = self.new_user_read.text()
        if username != "":
            if not User.user_exists(username):
                access_right = self.access_right_read_3.currentText()
                access_right = int(access_right[0])
                User.modify_user(self.username, username, access_right)
                self.new_user_read.setEnabled(False)
                self.access_right_read_3.setEnabled(False)
                self.modify_button_2.setEnabled(False)
                self.search_user_read.clear()
            else:
                QMessageBox.critical(self, 'Username already exists.', 'Please enter a unique username and try again.')
        else:
            QMessageBox.warning(self, 'Blank input', 'Please enter a valid Username.')
            
    def changePassword(self):
        old_password = self.old_password.text()
        username = self.username_read_3.text()
        new_password = self.new_password.text()
        new_password2 = self.new_password2.text()
        if User.user_exists(username):
            if new_password == new_password2:
                access = User.verify_password(username, old_password)
                if access is not None:
                    User.delete_user(username)
                    User.register_user(username, new_password, access)
                    QMessageBox.information(self, 'Password changed', f'The password for {username} has been changed successfully.')
                else:
                    QMessageBox.critical(self, 'Authentication failed', 'Wrong Password')
            else:
                QMessageBox.warning(self, 'Password mismatch', 'Please make sure that your passwords match.')
        else:
            QMessageBox.warning(self, 'User not found', 'The specified user does not exist.')
            

    def changeThemeLight(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        stylesheet_path = os.path.join(current_dir, "QSS-master", "Ubuntu.qss")
        self.loadStylesheet(stylesheet_path)

    def changeThemeAqua(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        stylesheet_path = os.path.join(current_dir, "QSS-master", "ManjaroMix.qss")
        self.loadStylesheet(stylesheet_path)

    def changeThemeDark(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        stylesheet_path = os.path.join(current_dir, "QSS-master", "MaterialDark.qss")
        self.loadStylesheet(stylesheet_path)

    def changeThemeConsole(self):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        stylesheet_path = os.path.join(current_dir, "QSS-master", "ConsoleStyle.qss")
        self.loadStylesheet(stylesheet_path)

        
    def passwordModeChange(self, state):
        if state:
            self.password_read.setEchoMode(QLineEdit.EchoMode.Normal)
            self.password2_read.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.password_read.setEchoMode(QLineEdit.EchoMode.Password)
            self.password2_read.setEchoMode(QLineEdit.EchoMode.Password)
            
        
class WelcomeScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file_path = os.path.join(current_dir, "welcome.ui")
        loadUi(ui_file_path, self)
        
        

class LoginUi(QWidget):
    login_successful = pyqtSignal(str, int)
    def __init__(self, parent = None):
        super().__init__(parent)
        current_dir = os.path.dirname(os.path.abspath(__file__))
        ui_file_path = os.path.join(current_dir, "Login.ui")
        loadUi(ui_file_path, self)
        self.loginbutton.clicked.connect(self.login)

    def login(self):
        username = self.userinput.text()
        password = self.passwordinput.text()
        access = User.verify_password(username, password)

        if access is not None:
            self.login_successful.emit(username, access)
        else:
            QMessageBox.warning(self, 'Login', 'Invalid Username or Password')

        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyGUI()
    window.show()
    sys.exit(app.exec())



