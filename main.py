from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QFont

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator App")
main_window.resize(250, 300)

text_box = QLineEdit()
grid = QGridLayout()

buttons = ["7", "8", "9", "/", 
           "4", "5", "6", "*", 
           "1", "2", "3", "-", 
           "0", ".", "=", "+"]

clear = QPushButton("C")
delete = QPushButton("Del")

# Function to handle button clicks
def button_click():
    button = app.sender()
    text = button.text()
    
    if text == "=":
        symbol = text_box.text()
        try:
            # Evaluate the expression
            res = eval(symbol)
            
            # Format the result with commas
            formatted_res = "{:,}".format(res)
            
            # Set the result in the text box with bold, larger font
            text_box.setText(formatted_res)
            text_box.setFont(QFont("Arial", 14, QFont.Bold))  # Set larger, bold font
            
        except Exception as e:
            text_box.setText("Error")
            text_box.setFont(QFont("Arial", 14, QFont.Bold))  # Bold font for error
            
    elif text == "C":
        text_box.clear()
        text_box.setFont(QFont())  # Reset to default font
        
    elif text == "Del":
        current_text = text_box.text()
        text_box.setText(current_text[:-1])
    else:
        current_text = text_box.text()
        text_box.setText(current_text + text)

# Create the grid layout for buttons
row = 0
col = 0

for text in buttons:
    button = QPushButton(text)
    button.clicked.connect(button_click)
    grid.addWidget(button, row, col)
    
    col += 1
    
    if col > 3:
        col = 0
        row += 1

# Main layout
master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid)

button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)

master_layout.addLayout(button_row)
main_window.setLayout(master_layout)

clear.clicked.connect(button_click)
delete.clicked.connect(button_click)

main_window.show()
app.exec_()