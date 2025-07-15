# Imports
from PyQt5.QtWidgets import QApplication,QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
# App settings
app =QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator App")
main_window.resize(250,300)

#All objects/widgets

text_box = QLineEdit()
grid = QGridLayout()

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
    ]
clear = QPushButton("Clear")
delete = QPushButton("<")

# Design



# Show/Run
main_window.show()
app.exec()