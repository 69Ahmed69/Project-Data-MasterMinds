from ast import Lambda
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QPushButton, QWidget, QVBoxLayout, QLabel, QLineEdit
from PyQt6.QtGui import QColor, QFont
from PyQt6.QtCore import pyqtSignal, QSize, Qt



class Table(QMainWindow):
    preferences_updated = pyqtSignal(list)
    def __init__(self, preferences, name, surname, age, exp, nbr_hours, courses):
        super().__init__()

        self.setWindowTitle("Dr. "+ name+" "+surname+"'s data")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background-color: #141414; color: #ffffff; font-size: 10pt; font-family: Bahnschrift")
        self.preferences = preferences
        widget = QWidget(self)
        layout = QVBoxLayout(widget)
        widget.setLayout(layout)
        name_label = QLabel(f"Dr.{name} {surname}")
        name_label.setStyleSheet("font-size: 18pt;font-family: MS Shell Dlg 2;")
        layout.addWidget(name_label)
        age_label = QLabel(f"Age: {age}")
        age_label.setStyleSheet("font-size: 18pt;font-family: MS Shell Dlg 2;")
        layout.addWidget(age_label)
        exp_label = QLabel(f"Experience: {exp}")
        exp_label.setStyleSheet("font-size: 18pt;font-family: MS Shell Dlg 2;")
        layout.addWidget(exp_label)
        nbr_hours_label = QLabel(f"Number of Hours: {nbr_hours if nbr_hours != 0 else '0'}")
        nbr_hours_label.setStyleSheet("font-size: 18pt;font-family: MS Shell Dlg 2;")
        layout.addWidget(nbr_hours_label)
        courses_label_text = "This teacher is useless" if courses == 0 or courses is None else "This teacher is not useless"
        courses_label = QLabel(courses_label_text)
        courses_label.setStyleSheet("font-size: 18pt;font-family: MS Shell Dlg 2;")
        layout.addWidget(courses_label)
        widget.setGeometry(50, 350, 300, 200)
        self.table_widget = QTableWidget(self)
        self.table_widget.setGeometry(41, 0, 718, 349)
        self.table_widget.setRowCount(7)
        self.table_widget.setColumnCount(7)
        self.table_widget.setStyleSheet("border: none;color: #f0f0f0; font-family: Arial Black;")  
        for row in range(self.table_widget.rowCount()):
            self.table_widget.setRowHeight(row, 42)                                                                                                                                                                                                                                                                                                                                                                                    
        # Populate table with buttons
        for row in range(self.table_widget.rowCount()):
            for col in range(self.table_widget.columnCount()):
                if row == 0:
                    if col == 0:
                        item = QTableWidgetItem("Days/Time")
                        item.setBackground(QColor(50, 50, 50))
                        self.table_widget.setItem(row, col, item)
                    if col == 1:
                        item = QTableWidgetItem("8:00")
                        item.setBackground(QColor(50, 50, 50))
                        self.table_widget.setItem(row, col, item)
                    if col == 2:
                        item = QTableWidgetItem("9:35")
                        item.setBackground(QColor(50, 50, 50))
                        self.table_widget.setItem(row, col, item)
                    if col == 3:
                        item = QTableWidgetItem("11:10")
                        item.setBackground(QColor(50, 50, 50))
                        self.table_widget.setItem(row, col, item)
                    if col == 4:
                        item = QTableWidgetItem("12:45")
                        item.setBackground(QColor(50, 50, 50))
                        self.table_widget.setItem(row, col, item)
                    if col == 5:
                        item = QTableWidgetItem("14:20")
                        item.setBackground(QColor(50, 50, 50))
                        self.table_widget.setItem(row, col, item)
                    if col == 6:
                        item = QTableWidgetItem("15:50")
                        item.setBackground(QColor(50, 50, 50))
                        self.table_widget.setItem(row, col, item)
                elif col == 0:
                    if row == 1:
                        item = QTableWidgetItem("Sunday")
                        item.setBackground(QColor(100, 100, 100))
                        self.table_widget.setItem(row, col, item)
                    if row == 2:
                        item = QTableWidgetItem("Monday")
                        item.setBackground(QColor(100, 100, 100))
                        self.table_widget.setItem(row, col, item)
                    if row == 3:
                        item = QTableWidgetItem("Tuesday")
                        item.setBackground(QColor(100, 100, 100))
                        self.table_widget.setItem(row, col, item)
                    if row == 4:
                        item = QTableWidgetItem("Wednesday")
                        item.setBackground(QColor(100, 100, 100))
                        self.table_widget.setItem(row, col, item)
                    if row == 5:
                        item = QTableWidgetItem("Thursday")
                        item.setBackground(QColor(100, 100, 100))
                        self.table_widget.setItem(row, col, item)
                    if row == 6:
                        item = QTableWidgetItem("Saturday")
                        item.setBackground(QColor(100, 100, 100))
                        self.table_widget.setItem(row, col, item)
                else:
                    button = QPushButton(f"{preferences[row-1][col-1]}")
                    button.clicked.connect(lambda: self.button_clicked(preferences))
                    button.setCursor(Qt.CursorShape.PointingHandCursor)
                    color = self.setButtonColor(preferences[row-1][col-1])
                    button.setStyleSheet(f"background-color: rgb({color.red()}, {color.green()}, {color.blue()}); font-weight: 400;")
                    self.table_widget.setCellWidget(row, col, button)
        #self.table_widget.setShowGrid(False)
        save_button = QPushButton("Save Changes", self)
        save_button.setGeometry(600, 400, 150, 40)
        save_button.setCursor(Qt.CursorShape.PointingHandCursor)
        save_button.setStyleSheet("background-color: #202020; border-radius: 15px;font-size: 14px; font-weight: bold;")
        save_button.clicked.connect(lambda: self.save_changes(preferences))
        close_button = QPushButton("Close", self)
        close_button.setStyleSheet("background-color: #202020; border-radius: 15px;font-size: 14px; font-weight: bold;")
        close_button.setGeometry(600, 450, 150, 40)
        close_button.setCursor(Qt.CursorShape.PointingHandCursor)
        close_button.clicked.connect(lambda: self.close_window(preferences))

    def setButtonColor(self, num):
        if num == 0:
            color = QColor(180, 8, 8)
        elif num == 1:
            color = QColor(255, 130, 31)
        elif num == 2:
            color = QColor(228, 208, 10)
        elif num == 3:
            color = QColor(15, 162, 8)
        else:
            color = QColor(2, 100, 32)
        return color

    def close_window(self, preferences):
        self.preferences_updated.emit(preferences)  # Emit the signal with preferences
        self.close()
    
    def save_changes(self, preferences):
        for row in range(1, self.table_widget.rowCount()):
            for col in range(1, self.table_widget.columnCount()):
                widget = self.table_widget.cellWidget(row, col)
                if isinstance(widget, QPushButton):
                    preferences[row-1][col-1] = int(widget.text()) if widget.text().isdigit() else 0
        print("Changes saved:", preferences)
    


    def button_clicked(self, preferences):
        button = self.sender()
        if isinstance(button, QPushButton):
            row, col = self.table_widget.indexAt(button.pos()).row(), self.table_widget.indexAt(button.pos()).column()
            current_value = int(button.text()) 
            new_value = (current_value + 1) % 5 
            button.setText(str(new_value))
            color = self.setButtonColor(new_value)
            button.setStyleSheet(f"background-color: rgb({color.red()}, {color.green()}, {color.blue()})")
            preferences[row-1][col-1] = new_value
    
def handlePreferencesUpdated(bst, prof, preferences):
    prof.preferences = preferences
    bst.saveProfToCsv()