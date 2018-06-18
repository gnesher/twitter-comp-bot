import MySQLdb
import tweepy
import sqlite3
import time
import re

from local_settings import (CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,
                            ACCESS_SECRET)

if __name__ == '__main__':
    auth = tweepy.auth.OAuthHandler(
        consumer_key='',
        consumer_secret='')
    auth.set_access_token(
        '',
        '')

    api = tweepy.API(auth_handler=auth)

    for friend in tweepy.Cursor(api.friends).items():
        friend.unfollow()
        print friend.screen_name
        time.sleep(5)
