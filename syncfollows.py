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


if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM ' + DB_PREFIX + 'follows')
    followers = cursor.fetchall()
    db_follower_ids = [follower[0] for follower in followers]
    twitter_follower_ids = api.friends_ids()
    # first remove all followers in db that are not in your twitter friends list
    for db_follower in db_follower_ids:
        if int(db_follower) not in twitter_follower_ids:
            cursor.execute("DELETE FROM " + DB_PREFIX + "follows WHERE author_id=%s LIMIT 1", [db_follower])
            db.commit()
            print 'follow in db not in twitter, removing %s' % db_follower
    for twitter_follower in twitter_follower_ids:
        if str(twitter_follower) not in db_follower_ids:
            try:
                api.destroy_friendship(id=twitter_follower)
                print 'follow in twitter not in db, unfollowing %s' % twitter_follower
            except Exception as e:
                print 'unable to unfollow', e
            time.sleep(5)
        else:
            print 'follower %s is correct', twitter_follower
