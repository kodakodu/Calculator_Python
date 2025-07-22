# Imports
from PyQt5.QtWidgets import (QApplication,QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout)
# App settings
app =QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator App")
main_window.resize(250,300)

#All objects/widgets

text_box= QLineEdit()
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


master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
#master_layout.addWidget(grid)

button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)

master_layout.addWidget(button_row)



main_window.setLayout(master_layout)


# Show/Run
main_window.show()
app.exec()