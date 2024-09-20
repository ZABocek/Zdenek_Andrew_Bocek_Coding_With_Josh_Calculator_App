from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtGui import QFont

class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator App")
        self.resize(250, 300)
        
        # Create the text box for displaying input/output
        self.text_box = QLineEdit()
        
        # Create the grid layout for buttons
        self.grid = QGridLayout()
        self.buttons = ["7", "8", "9", "/", 
                        "4", "5", "6", "*", 
                        "1", "2", "3", "-", 
                        "0", ".", "=", "+"]
        self.clear = QPushButton("C")
        self.delete = QPushButton("Del")

        # Initialize UI components
        self.init_ui()
    
    def init_ui(self):
        """ Setup the UI elements and layout. """
        row = 0
        col = 0
        
        # Create buttons and add them to the grid layout
        for text in self.buttons:
            button = QPushButton(text)
            button.clicked.connect(self.button_click)
            self.grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        # Main layout
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        # Add clear and delete buttons
        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)
        master_layout.addLayout(button_row)

        self.setLayout(master_layout)

        # Connect clear and delete buttons to their functions
        self.clear.clicked.connect(self.button_click)
        self.delete.clicked.connect(self.button_click)
    
    def format_text(self, text):
        """ Helper function to format numbers with commas. """
        try:
            if "." in text:
                parts = text.split(".")
                parts[0] = "{:,}".format(int(parts[0]))  # Add commas to integer part
                return ".".join(parts)
            else:
                return "{:,}".format(int(text))  # If there's no decimal, format the number
        except ValueError:
            return text  # If the input is not purely numeric (e.g., has operators), return as is
    
    def button_click(self):
        """ Handle button clicks. """
        button = self.sender()
        text = button.text()
        
        if text == "=":
            symbol = self.text_box.text().replace(",", "")  # Remove commas for eval
            try:
                res = eval(symbol)
                formatted_res = "{:,}".format(res)
                self.text_box.setText(formatted_res)
                self.text_box.setFont(QFont("Arial", 14, QFont.Bold))  # Larger, bold font
            except Exception:
                self.text_box.setText("Error")
                self.text_box.setFont(QFont("Arial", 14, QFont.Bold))  # Bold font for error
        elif text == "C":
            self.text_box.clear()
            self.text_box.setFont(QFont())  # Reset to default font
        elif text == "Del":
            current_text = self.text_box.text().replace(",", "")
            self.text_box.setText(self.format_text(current_text[:-1]))  # Remove last char and reformat
        else:
            current_text = self.text_box.text().replace(",", "")  # Remove commas for accurate input
            new_text = current_text + text
            self.text_box.setText(self.format_text(new_text))  # Update with formatted text
            self.text_box.setFont(QFont("Arial", 14, QFont.Bold))  # Apply bold font


# Run the calculator app
if __name__ == "__main__":
    app = QApplication([])
    calculator = CalculatorApp()
    calculator.show()
    app.exec_()
    