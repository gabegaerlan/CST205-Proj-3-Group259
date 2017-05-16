import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QProgressBar, QLabel
from PyQt5.QtGui import QIcon
import codecs
from datetime import datetime
from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRestPager

consumer_key= "BIZ0ZdufeLfvqwyTSEJxA1kLe"
consumer_secret= "EC4UADiivdunzTs2nu6ssSHyjcukU5QjQxBUQwXaN9N6hxyFuv"
access_token_key= "849323701472505858-fpNmEs3iTT8PXjj3LCOKFarwMY52ela"
access_token_secret= "omC5iblhvvPEhaIeIVCN4XDUGldd3ol1TcWY2MkrGNhdK"

# Using OAuth1...
api = TwitterAPI(consumer_key,
                 consumer_secret,
                 access_token_key,
                 access_token_secret)


# def post_tweet(message):

class Second_window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Second Window test'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.init_ui()

    def init_ui(self):
        booton = QPushButton('Nothing', self)
        booton.move(60, 100)
        self.setWindowTitle('Second Window test')
        self.show()

class Window(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        # self.left = 10
        # self.top = 10
        # self.width = 400
        # self.height = 140
        self.init_ui()
    
    def init_ui(self):
        
        load1 = False
        load2 = False
        myButton = QPushButton('Check', self)
        #myButton.move(60,100)
        #self.myLabel = QtWidgets.QLabel('Button not clicked yet')
        self.textbox = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        #self.textbox.move(50,50)
        self.progress = QProgressBar(self)
        self.label = QLabel('Complete')
        
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.textbox)
        h_box.addStretch()
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.textbox)
        v_box.addWidget(self.textbox2)
        v_box.addWidget(myButton)
        v_box.addWidget(self.progress)
        if(load1 == True & load2 == True):
            v_box.addWidget(self.label)
        v_box.addLayout(h_box)
        
        self.setLayout(v_box)
        self.setWindowTitle('Conversation Check!')
        
        # create connection between signal (click) and slot (stuff in parens)
        myButton.clicked.connect(self.btn_click)
        # self.dialog = Second_window(self)
        
        self.show()
    
    def btn_click(self):
        # window = Second_window()
        # self.close()
        self.completed = 0
        while self.completed < 100:
            self.completed += 0.0001
            self.progress.setValue(self.completed)
        textboxValue = self.textbox.text() + ' ' + self.textbox2.text()
        print(textboxValue)
        # post_tweet(textboxValue)
        for item in api.request('search/tweets', {'q': textboxValue, 'count': 5}):
            print(item['text'] if 'text' in item else item)
        load1 = True
        load2 = True
        self.sw = Second_window()
        self.hide()
        self.sw.show()

        #print(r.status_code)

# create application loop
app = QtWidgets.QApplication(sys.argv)

# create instance of Window class
a_window = Window()
sys.exit(app.exec_())