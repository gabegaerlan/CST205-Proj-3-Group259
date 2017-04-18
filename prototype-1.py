import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
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


def post_tweet(message):
    r = api.request('statuses/update',
                            {'status': message})
    print(r.status_code)


class Window(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        # self.title = 'PyQt5 textbox - pythonspot.com'
        # self.left = 10
        # self.top = 10
        # self.width = 400
        # self.height = 140
        self.init_ui()
    
    #def textbox(self):
    
    
    def init_ui(self):
        myButton = QPushButton('Tweet', self)
        #myButton.move(60,100)
        #self.myLabel = QtWidgets.QLabel('Button not clicked yet')
        self.textbox = QLineEdit(self)
        #self.textbox.move(50,50)
        
        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addWidget(self.textbox)
        h_box.addStretch()
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(myButton)
        v_box.addWidget(self.textbox)
        v_box.addLayout(h_box)
        
        self.setLayout(v_box)
        self.setWindowTitle('Base Tweet App')
        
        # create connection between signal (click) and slot (stuff in parens)
        myButton.clicked.connect(self.btn_click)
        
        self.show()
    
    def btn_click(self):
        textboxValue = self.textbox.text()
        post_tweet(textboxValue)

# create application loop
app = QtWidgets.QApplication(sys.argv)

# create instance of Window class
a_window = Window()
sys.exit(app.exec_())