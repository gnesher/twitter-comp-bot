#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import MySQLdb
import json
from datetime import datetime
import time
import sys
import re

from constants import (IGNORED_KEYWORDS, IGNORED_USERS, QUERY,
                       USER_STREAM, POSITIVE_KEYWORDS, TABLE_PREFIXES)
from local_settings import (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME,
                            CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,
                            ACCESS_SECRET, STACK, DB_PREFIX)

# Set DB connection
db = MySQLdb.connect(host=DB_HOST,
                     user=DB_USER,
                     passwd=DB_PASSWORD,
                     db=DB_NAME,
                     use_unicode=True,)

db.set_character_set('utf8mb4')
cursor = db.cursor()
cursor.execute("SET NAMES utf8mb4")
cursor.execute("SET CHARACTER SET utf8mb4")
cursor.execute("SET character_set_connection=utf8mb4")

retweets_to_populate = []

# Basic Matching for new tweets:
# 1. Is a retweet
# 2. original tweet author isn't in our banned user list
def is_good_tweet(tweet):
    if not hasattr(tweet, 'retweeted_status'):
        return False
    if tweet.retweeted_status.user.id in IGNORED_USERS:
        return False

    return True


def no_ignored_keywords(tweet):
    text = tweet.retweeted_status.text
    clean_text = re.sub(r'([^\s\w]|_)+', '', text).lower()
    clean_text.replace('#', '')
    tweet_text_dict = [word for word in clean_text.split(" ")]
    if any(map(lambda v: v in tweet_text_dict, IGNORED_KEYWORDS)):
        return False
    
    if any(map(lambda v: v in tweet_text_dict, POSITIVE_KEYWORDS)):
        return True

    return False


# This is the listener, responsible for receiving data
class StdOutListener(tweepy.StreamListener):

    def on_data(self, data):

        global retweets_to_populate
        decoded = json.loads(data)
        if (is_good_tweet(decoded) and no_ignored_keywords(decoded)):
            tweet_text = decoded['retweeted_status']['text'].encode('utf-8')
            time_zone = decoded['retweeted_status']['user']['time_zone']
            if time_zone is not None:
                time_zone.encode('utf-8')
            location = decoded['retweeted_status']['user']['location']
            if location is not None:
                location.encode('utf-8')
            retweets_to_populate.append((
                decoded['retweeted_status']['id'],
                tweet_text,
                datetime.strptime(decoded['retweeted_status']['created_at'], '%a %b %d %H:%M:%S +0000 %Y'),
                decoded['retweeted_status']['user']['id'],
                time_zone,
                location,
                decoded['retweeted_status']['user']['url'],
                0,
            ))
            if len(retweets_to_populate) > 10:
                for prefix in TABLE_PREFIXES:
                    cursor.executemany('INSERT IGNORE INTO ' + prefix + '_retweets(tweet_id, tweet_text, tweet_time, author_id, time_zone, location, url, status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', retweets_to_populate)
                    db.commit()
                retweets_to_populate = []

    def on_error(self, status_code):
        print 'Encountered error with status code:' + repr(status_code.encode('utf-8'))
        return True

    def on_disconnect(self, notice):
        print 'disconnected from twitter:' + repr(notice.encode('utf-8'))
        return True

    def on_timeout(self):
        print 'Timeout...'
        return True


def itterate_users():
    while True:
        for userID in USER_STREAM:
            retweets_to_populate = []
            user_tweets = api.user_timeline(id = userID, count = 50, include_rts = True)
            for tweet in user_tweets:
                if (is_good_tweet(tweet) and no_ignored_keywords(tweet)):
                    tweet_text = tweet.retweeted_status.text.encode('utf-8')
                    time_zone = tweet.retweeted_status.user.time_zone
                    if time_zone is not None:
                        time_zone.encode('utf-8')
                    location = tweet.retweeted_status.user.location
                    if location is not None:
                        location.encode('utf-8')
                    retweets_to_populate.append((
                        tweet.retweeted_status.id,
                        tweet_text,
                        tweet.retweeted_status.created_at,
                        tweet.retweeted_status.user.id,
                        time_zone,
                        location,
                        tweet.retweeted_status.user.url,
                        0,
                    ))
                '''
                else:
                    if  hasattr(tweet, 'retweeted_status'):
                        print tweet.retweeted_status.text.encode('utf-8')
                    else:
                        print 'not a retweet ---->', tweet.text
                '''
            for prefix in TABLE_PREFIXES:
                cursor.executemany('INSERT IGNORE INTO ' + prefix + '_retweets(tweet_id, tweet_text, tweet_time, author_id, time_zone, location, url, status) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)', retweets_to_populate)
                db.commit()
            time.sleep(20)



if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    itterate_users()
    db.close()
