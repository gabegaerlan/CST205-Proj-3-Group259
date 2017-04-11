import codecs
from datetime import datetime
import sys
from TwitterAPI import TwitterAPI, TwitterOAuth, TwitterRestPager
import easygui

TEST_NUMBER = 6

def start():
    image = "zbobby.jpg"
    msg = "Select option"
    choices = ["Authenticate", "Post time/date", "Search for key phrase", "Stream tweets from NYC", "Get tweets from past week with key phrase", "upload image"]
    reply = easygui.buttonbox(msg, image=image, choices=choices)
    if reply == choices[0]:
        equal0()
    elif reply == choices[1]:
        equal1()
    elif reply == choices[2]:
        equal2()
    elif reply == choices[3]:
        equal3()
    elif reply == choices[4]:
        equal4()
    elif reply == choices[5]:
        equal5()


def equal0():
    # VERIFY YOUR CREDS
    r = api.request('account/verify_credentials')
    print(r.text)

def equal1():
    # POST A TWEET
    r = api.request('statuses/update',
                    {'status': 'the time is now %s' % datetime.now()})
    print(r.status_code)

def equal2():
    # GET 5 TWEETS CONTAINING 'ZZZ'
    for item in api.request('search/tweets', {'q': 'zzz', 'count': 5}):
        print(item['text'] if 'text' in item else item)

def equal3():
    # STREAM TWEETS FROM AROUND NYC
    for item in api.request('statuses/filter', {'locations': '-74,40,-73,41'}):
        print(item['text'] if 'text' in item else item)

def equal4():
    # GET TWEETS FROM THE PAST WEEK OR SO CONTAINING 'LOVE'
    pager = TwitterRestPager(api, 'search/tweets', {'q': 'love'})
    for item in pager.get_iterator():
        print(item['text'] if 'text' in item else item)

def equal5():
    file = open(IMAGE_PATH, 'rb')
    data = file.read()
    r = api.request('statuses/update_with_media',
                    {'status': TWEET_TEXT},
                    {'media[]': data})
                    
    print('SUCCESS' if r.status_code == 200 else 'FAILURE')



try:
    # python 3
    sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
except:
    # python 2
    sys.stdout = codecs.getwriter('utf8')(sys.stdout)


# SAVE YOUR APPLICATION CREDENTIALS IN TwitterAPI/credentials.txt.
# o = TwitterOAuth.read_file()

consumer_key= "BIZ0ZdufeLfvqwyTSEJxA1kLe"
consumer_secret= "EC4UADiivdunzTs2nu6ssSHyjcukU5QjQxBUQwXaN9N6hxyFuv"
access_token_key= "849323701472505858-fpNmEs3iTT8PXjj3LCOKFarwMY52ela"
access_token_secret= "omC5iblhvvPEhaIeIVCN4XDUGldd3ol1TcWY2MkrGNhdK"
IMAGE_PATH = "zbobby.jpg"
TWEET_TEXT = "Finally a selfie 4 my woes"

# Using OAuth1...
api = TwitterAPI(consumer_key,
               consumer_secret,
               access_token_key,
               access_token_secret)

# Using OAuth2...
# api = TwitterAPI(consumer_key, consumer_secret, auth_type="oAuth2")


start()
# print TEST_NUMBER



"""try:
    if TEST_NUMBER == 0:

        # VERIFY YOUR CREDS
        r = api.request('account/verify_credentials')
        print(r.text)

    if TEST_NUMBER == 1:

        # POST A TWEET
        r = api.request('statuses/update',
                        {'status': 'the time is now %s' % datetime.now()})
        print(r.status_code)

    if TEST_NUMBER == 2:

        # GET 5 TWEETS CONTAINING 'ZZZ'
        for item in api.request('search/tweets', {'q': 'zzz', 'count': 5}):
            print(item['text'] if 'text' in item else item)

    if TEST_NUMBER == 3:

        # STREAM TWEETS FROM AROUND NYC
        for item in api.request('statuses/filter', {'locations': '-74,40,-73,41'}):
            print(item['text'] if 'text' in item else item)

    if TEST_NUMBER == 4:

        # GET TWEETS FROM THE PAST WEEK OR SO CONTAINING 'LOVE'
        pager = TwitterRestPager(api, 'search/tweets', {'q': 'love'})
        for item in pager.get_iterator():
            print(item['text'] if 'text' in item else item)

    if TEST_NUMBER == 5:
        file = open(IMAGE_PATH, 'rb')
        data = file.read()
        r = api.request('statuses/update_with_media',
                {'status': TWEET_TEXT},
                {'media[]': data})

        print('SUCCESS' if r.status_code == 200 else 'FAILURE')

except Exception as e:
    print(e)"""
