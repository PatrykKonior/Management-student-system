import sys
from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, \
    QLineEdit, QPushButton, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Student Management System")
