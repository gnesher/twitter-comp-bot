# make sure db follows match twitter follows

import MySQLdb
import tweepy
import sqlite3
import time
import re

from local_settings import (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME,
                            CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,
                            ACCESS_SECRET, DB_PREFIX)

# Set DB connection
db = MySQLdb.connect(host=DB_HOST,
                     user=DB_USER,
                     passwd=DB_PASSWORD,
                     db=DB_NAME,
                     use_unicode=True)


cursor = db.cursor()

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    twitter_follower_ids = api.friends_ids()
    for twitter_follower in twitter_follower_ids:
        cursor.execute(
            "REPLACE into " + DB_PREFIX +
            "follows (author_id, last_tweet_follow) VALUES (%s, NOW())",
            [twitter_follower]
        )
        db.commit()
        print 'added follower from twitter to db'
