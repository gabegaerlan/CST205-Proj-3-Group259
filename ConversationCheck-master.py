import sys
import codecs
from PyQt5.QtWidgets import *
from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRestPager

consumer_key= "BIZ0ZdufeLfvqwyTSEJxA1kLe"
consumer_secret= "EC4UADiivdunzTs2nu6ssSHyjcukU5QjQxBUQwXaN9N6hxyFuv"
access_token_key= "849323701472505858-fpNmEs3iTT8PXjj3LCOKFarwMY52ela"
access_token_secret= "omC5iblhvvPEhaIeIVCN4XDUGldd3ol1TcWY2MkrGNhdK"

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

textboxValue = ' '
first_user = ' '
sec_user = ' '
tweet_amount = 5

class Window(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.init_ui()
    
    def init_ui(self):
        self.lbl_intro = QLabel('Welcome!')
        self.lbl_enter_user1 = QLabel('First User:')
        self.lbl_enter_user2 = QLabel('Second User:')
        self.lbl_enter_amount = QLabel('Amount of Tweets: ')
        self.txt_enter_user1 = QLineEdit('@')
        self.txt_enter_user2 = QLineEdit('@')
        self.num_enter_amount = QComboBox()
        #self.cb_login = QCheckBox('Stay logged in?')
        self.btn_login = QPushButton('Check')
        
        self.num_enter_amount.addItem('1')
        self.num_enter_amount.addItem('2')
        self.num_enter_amount.addItem('3')
        self.num_enter_amount.addItem('4')
        self.num_enter_amount.addItem('5')
        self.num_enter_amount.addItem('6')
        self.num_enter_amount.addItem('7')
        self.num_enter_amount.addItem('8')
        
        self.grid = QGridLayout()
        self.grid.setSpacing(5)
        
        self.grid.addWidget(self.lbl_intro, 1, 1)
        
        self.grid.addWidget(self.lbl_enter_user1, 2, 0)
        self.grid.addWidget(self.txt_enter_user1, 2, 1)
        
        self.grid.addWidget(self.lbl_enter_user2, 3, 0)
        self.grid.addWidget(self.txt_enter_user2, 3, 1)
        
        self.grid.addWidget(self.lbl_enter_amount, 4, 0)
        self.grid.addWidget(self.num_enter_amount, 4, 1)
        
        self.grid.addWidget(self.btn_login, 5, 1)
        
        
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
        
        self.setWindowTitle('Conversation Check')
        
        self.show()
    
    def btn_login_clk(self):
        global textboxValue
        textboxValue = self.txt_enter_user1.text() + ' ' + self.txt_enter_user2.text()
        global first_user
        first_user = self.txt_enter_user1.text()
        global sec_user
        sec_user = self.txt_enter_user2.text()
        self.mw = MainWindow()
        self.hide()
        self.mw.show()
    
    
    def clear_box(self):
        self.txt_enter_user1.clear()
        self.txt_enter_user2.clear()


class MainWindow(Window):
    
    def __init__(self):
        super().__init__()
        
        self.init_ui()
    
    def init_ui(self):
        count_var = 0
        TweetList = [0,1,2,3,4,5,6,7,8]
        self.lbl_intro = QLabel('Tweets from: ' + textboxValue)
            #for thing in api.request('search/tweets', {'q': first_user, 'count': 1000}):
        for item in api.request('search/tweets', {'q': textboxValue, 'count': tweet_amount}):
            TweetList[count_var] = item['text'] if 'text' in item else item
            count_var = count_var + 1
        #print(item['text'] if 'text' in item else item)
        self.contents = QLabel(TweetList[0])
        if(tweet_amount > 1):
            self.contents1 = QLabel(TweetList[1])
            if(tweet_amount > 2):
                self.contents2 = QLabel(TweetList[2])
                if(tweet_amount > 3):
                    self.contents3 = QLabel(TweetList[3])
                    if(tweet_amount > 4):
                        self.contents4 = QLabel(TweetList[4])
                        if(tweet_amount > 5):
                            self.contents5 = QLabel(TweetList[5])
                            if(tweet_amount > 6):
                                self.contents6 = QLabel(TweetList[6])
                                if(tweet_amount > 7):
                                    self.contents7 = QLabel(TweetList[7])
        self.btn_exit = QPushButton('Exit')
        
        layout = QVBoxLayout()
        layout.addWidget(self.lbl_intro)
        layout.addWidget(self.contents)
        if(tweet_amount > 1):
            layout.addWidget(self.contents1)
            if(tweet_amount > 2):
                layout.addWidget(self.contents2)
                if(tweet_amount > 3):
                    layout.addWidget(self.contents3)
                    if(tweet_amount > 4):
                        layout.addWidget(self.contents4)
                        if(tweet_amount > 5):
                            layout.addWidget(self.contents5)
                            if(tweet_amount > 6):
                                layout.addWidget(self.contents6)
                                if(tweet_amount > 7):
                                    layout.addWidget(self.contents7)
        layout.addWidget(self.btn_exit)
        
        self.setLayout(layout)
        self.setWindowTitle('Main')
        
        self.btn_exit.clicked.connect(self.exit_action)
        
        self.show()
    
    
    def exit_action(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    a_window = Window()
    sys.exit(app.exec())