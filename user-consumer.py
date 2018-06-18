#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import MySQLdb
import re
import tweepy
from datetime import datetime

from constants import (IGNORED_KEYWORDS, IGNORED_USERS,
                       USER_STREAM, POSITIVE_KEYWORDS, TABLE_PREFIXES)
from local_settings import (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME,
                            CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,
                            ACCESS_SECRET)

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


# Basic Matching for new tweets:
# 1. Is a retweet
# 2. original tweet author isn't in our banned user list
def is_good_tweet(tweet_dict):
    if 'retweeted_status' not in tweet_dict:
        return False
    if tweet_dict['retweeted_status']['user']['id'] in IGNORED_USERS:
        return False

    return True


def no_ignored_keywords(tweet_dict):
    text = tweet_dict['retweeted_status']['text']
    clean_text = re.sub(r'([^\s\w]|_)+', '', text).lower()
    clean_text.replace('#', '')
    tweet_text_dict = [word for word in clean_text.split()]

    if any(v in IGNORED_KEYWORDS for v in tweet_text_dict):
        return False

    if any(v in POSITIVE_KEYWORDS for v in tweet_text_dict):
        return True

    return False


# This is the listener, responsible for receiving data
class StdOutListener(tweepy.StreamListener):
    def __init__(self, *args, **kwargs):
        super(StdOutListener, self).__init__(*args, **kwargs)
        self.retweets_to_populate = []

    def on_data(self, data):
        decoded = json.loads(data)
        if (is_good_tweet(decoded) and no_ignored_keywords(decoded)):
            tweet_text = decoded['retweeted_status']['text'].encode('utf-8')
            time_zone = decoded['retweeted_status']['user']['time_zone']
            if time_zone is not None:
                time_zone.encode('utf-8')
            location = decoded['retweeted_status']['user']['location']
            if location is not None:
                location.encode('utf-8')

            self.retweets_to_populate.append((
                decoded['retweeted_status']['id'],
                tweet_text,
                datetime.strptime(
                    decoded['retweeted_status']['created_at'],
                    '%a %b %d %H:%M:%S +0000 %Y'
                ),
                decoded['retweeted_status']['user']['id'],
                time_zone,
                location,
                decoded['retweeted_status']['user']['url'],
                0,
                'u-poller',
	    	decoded['retweeted_status']['user']['utc_offset']
            ))

            if len(self.retweets_to_populate) > 10:
                for prefix in TABLE_PREFIXES:
                    cursor.executemany('INSERT IGNORE INTO ' + prefix + '_retweets(tweet_id, tweet_text, tweet_time, author_id, time_zone, location, url, status, poller, utc_offset) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', self.retweets_to_populate)
                    db.commit()
                self.retweets_to_populate = []

    def on_error(self, status_code):
        print('Encountered error with status code: {}'.format(
            repr(status_code)))
        return True

    def on_disconnect(self, notice):
        print('disconnected from twitter: {}'.format(
            repr(notice)))
        return True

    def on_timeout(self):
        print('Timeout...')


if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    stream = tweepy.Stream(auth, l)
    stream.filter(follow=USER_STREAM)
    db.close()
