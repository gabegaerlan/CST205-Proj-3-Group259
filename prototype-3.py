import sys
from PyQt5.QtWidgets import *
from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRestPager

consumer_key= "BIZ0ZdufeLfvqwyTSEJxA1kLe"
consumer_secret= "EC4UADiivdunzTs2nu6ssSHyjcukU5QjQxBUQwXaN9N6hxyFuv"
access_token_key= "849323701472505858-fpNmEs3iTT8PXjj3LCOKFarwMY52ela"
access_token_secret= "omC5iblhvvPEhaIeIVCN4XDUGldd3ol1TcWY2MkrGNhdK"

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

class Window(QWidget):
    first_user = " "
    sec_user = " "
    
    def __init__(self):
        super().__init__()
        
        self.init_ui()
    
    def init_ui(self):
        self.lbl_intro = QLabel('Welcome!')
        self.lbl_enter_user1 = QLabel('First User:')
        self.lbl_enter_user2 = QLabel('Second User:')
        self.txt_enter_user1 = QLineEdit()
        self.txt_enter_user2 = QLineEdit()
        #self.cb_login = QCheckBox('Stay logged in?')
        self.btn_login = QPushButton('Check')
        
        
        self.grid = QGridLayout()
        self.grid.setSpacing(5)
        
        self.grid.addWidget(self.lbl_intro, 1, 1)
        
        self.grid.addWidget(self.lbl_enter_user1, 2, 0)
        self.grid.addWidget(self.txt_enter_user1, 2, 1)
        
        self.grid.addWidget(self.lbl_enter_user2, 3, 0)
        self.grid.addWidget(self.txt_enter_user2, 3, 1)
        
        #self.grid.addWidget(self.cb_login, 4, 1)
        self.grid.addWidget(self.btn_login, 4, 1)
        
        
        self.v_box = QVBoxLayout()
        self.v_box.addStretch(0)
        self.v_box.addLayout(self.grid)
        self.v_box.addStretch(0)
        
        self.h_box = QHBoxLayout()
        self.h_box.addStretch(0)
        self.h_box.addLayout(self.v_box)
        self.h_box.addStretch(0)
        
        self.setLayout(self.h_box)
        
        self.btn_login.clicked.connect(self.btn_login_clk)
        
        self.setWindowTitle('Login test')
        
        self.show()
    
    def btn_login_clk(self):
        textboxValue = self.txt_enter_user1.text() + ' ' + self.txt_enter_user2.text()
        for item in api.request('search/tweets', {'q': textboxValue, 'count': 5}):
            convo = item['text'] if 'text' in item else item
        print(convo)
        self.mw = MainWindow()
        self.hide()
        self.mw.show()


    def clear_box(self):
        self.txt_enter_username.clear()
        self.txt_enter_password.clear()
        self.txt_enter_username.setFocus()


class MainWindow(Window):
    
    def __init__(self):
        super().__init__()
        
        self.init_ui()
    
    def init_ui(self):
        self.lbl_intro = QLabel('Main Window')
        self.lbl_user_logged = QLabel('Welcome')
        self.lbl_append = QLabel('Write something')
        self.txt_write_box = QLineEdit()
        self.btn_append = QPushButton('Append')
        self.btn_logout = QPushButton('Logout')
        
        layout = QVBoxLayout()
        layout.addWidget(self.lbl_intro)
        layout.addWidget(self.lbl_user_logged)
        layout.addWidget(self.lbl_append)
        layout.addWidget(self.txt_write_box)
        layout.addWidget(self.btn_append)
        layout.addWidget(self.btn_logout)
        
        self.setLayout(layout)
        self.setWindowTitle('Main')
        
        self.btn_append.clicked.connect(self.append_clk)
        self.btn_logout.clicked.connect(self.logout_action)
        
        self.show()
    
    def append_clk(self):
        textboxValue = self.txt_write_box.text()
        for item in api.request('search/tweets', {'q': textboxValue, 'count': 5}):
            print(item['text'] if 'text' in item else item)
    
    def logout_action(self):
        self.close()
        a_window.show()
        a_window.clear_box()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a_window = Window()
    sys.exit(app.exec())