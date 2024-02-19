from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QMessageBox

class ComboBoxExample(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ComboBox Example")
        layout = QVBoxLayout()

        self.combobox = QComboBox()
        self.combobox.addItems(["Option 1", "Option 2", "Option 3"])
        self.combobox.currentTextChanged.connect(self.on_combobox_changed)  # Connect the signal to the function
        layout.addWidget(self.combobox)

        self.button = QPushButton("Get Selected Item")
        self.button.clicked.connect(self.get_selected_item)
        layout.addWidget(self.button)

        self.setLayout(layout)

    def on_combobox_changed(self, text):
        print(f"Selected item: {text}")

    def get_selected_item(self):
        selected_item = self.combobox.currentText()
        QMessageBox.information(self, "Selected Item", f"The selected item is: {selected_item}")

if __name__ == "__main__":
    app = QApplication([])
    window = ComboBoxExample()
    window.show()
    app.exec()