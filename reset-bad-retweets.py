import tweepy
import MySQLdb
import time
from itertools import izip_longest
from local_settings import (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME,
                            CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,
                            ACCESS_SECRET, DB_PREFIX)

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def cleanDB():
    cursor.execute('SELECT tweet_id FROM ' + DB_PREFIX + 'retweets where status=1 and tweet_time >= DATE_ADD(CURDATE(), INTERVAL -14 DAY) ORDER BY tweet_time DESC')
    tweets = [i[0] for i in cursor.fetchall()]
    groupedTweetIDs = grouper(tweets, 100, '')
    for group in groupedTweetIDs:
        try:
            fullTweets = api.statuses_lookup(group)
        except Exception as e:
            print e
        else:
            needFixing = []
            for tweet in fullTweets:
                if not tweet.retweeted:
                    needFixing.append(tweet.id_str)
            if len(needFixing) > 0:
                sql = 'UPDATE ' + DB_PREFIX + 'retweets SET status=0 where tweet_id in (%s)'
                formatedList = ', '.join(map(lambda x: '%s', needFixing))
                parsed = sql % formatedList
                updatedRows = cursor.execute(parsed, needFixing)
                db.commit()
                print needFixing, updatedRows
            else:
                print 'all tweets were correct'
            time.sleep(5)

if __name__ == '__main__':

    # set up tweepy
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    # Set DB connection
    db = MySQLdb.connect(host=DB_HOST,
                         user=DB_USER,
                         passwd=DB_PASSWORD,
                         db=DB_NAME,
                         use_unicode=True)

    cursor = db.cursor()
    cleanDB()
    db.close()
