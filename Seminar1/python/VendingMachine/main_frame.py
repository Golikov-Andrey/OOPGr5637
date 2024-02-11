from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QFont
import sys

class MainFrame(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("VendingMachines")
        self.setMaximumSize(300, 400)
        
        self.mainFont = QFont("Segoe print", 18, QFont.Bold)
        
        self.tfFirstName = QLineEdit()
        self.tfFirstName.setFont(self.mainFont)
        
        self.tfLastName = QLineEdit()
        self.tfLastName.setFont(self.mainFont)
        
        self.lbWelcome = QLabel()
        self.lbWelcome.setFont(self.mainFont)
        
        self.btnOk = QPushButton("Ok")
        self.btnOk.setFont(self.mainFont)
        self.btnOk.clicked.connect(self.on_ok_clicked)
        
        self.btnClear = QPushButton("Clear")
        self.btnClear.setFont(self.mainFont)
        self.btnClear.clicked.connect(self.on_clear_clicked)
        
        formLayout = QVBoxLayout()
        formLayout.addWidget(QLabel("First Name", font=self.mainFont))
        formLayout.addWidget(self.tfFirstName)
        formLayout.addWidget(QLabel("Last Name", font=self.mainFont))
        formLayout.addWidget(self.tfLastName)
        
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.btnOk)
        buttonLayout.addWidget(self.btnClear)
        
        mainLayout = QVBoxLayout()
        mainLayout.addLayout(formLayout)
        mainLayout.addWidget(self.lbWelcome)
        mainLayout.addLayout(buttonLayout)
        
        centralWidget = QWidget()
        centralWidget.setLayout(mainLayout)
        self.setCentralWidget(centralWidget)
        
        self.setStyleSheet("background-color: rgb(128, 128, 255);")
        
    def on_ok_clicked(self):
        firstName = self.tfFirstName.text()
        lastName = self.tfLastName.text()
        self.lbWelcome.setText("Hello " + firstName + " " + lastName)
        
    def on_clear_clicked(self):
        self.tfFirstName.setText("")
        self.tfLastName.setText("")
        self.lbWelcome.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myFrame = MainFrame()
    myFrame.show()
    sys.exit(app.exec_())