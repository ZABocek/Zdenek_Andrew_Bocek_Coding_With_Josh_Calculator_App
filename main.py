from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QGridLayout

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator App")
main_window.resize(250, 300)

main_window.show()
app.exec_()