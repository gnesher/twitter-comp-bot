#!/usr/bin/env python

import tweepy
import MySQLdb
import time
from random import randint
import raven
import re
import logging
import warnings
warnings.filterwarnings('error')

from constants import (EU_TIME_ZONES, EU_LOCATIONS, FOLLOW_INDICATORS, FILTER,
                       FAVOURITE_INDICATORS)
from local_settings import (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME,
                            CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY,
                            ACCESS_SECRET, DB_PREFIX)

logger = logging.getLogger(__name__)


def dict_factory(cursor, row):
    """
    Make a dict from a database row.
    """
    return {
        col[0]: row[idx]
        for idx, col in enumerate(cursor.description)
    }


def _tokenised_tweet(tweet_text):
    return re.sub(r'([^\s\w]|_)+', '', tweet_text).lower().split()


def needs_follow(tweet_text):
    return any(v in FOLLOW_INDICATORS for v in _tokenised_tweet(tweet_text))


def needs_fav(tweet_text):
    return any(v in FAVOURITE_INDICATORS for v in _tokenised_tweet(tweet_text))


def fetch_new_tweets_from_db(tz, lc):
    cursor.execute(FILTER)
    tweets = cursor.fetchall()
    cursor.execute('SELECT author_id FROM ' + DB_PREFIX + 'follows')
    followers_tuple = cursor.fetchall()
    followers = {follower[0] for follower in followers_tuple}
    for tweet in tweets:
        error = None
        status = 0

        if needs_follow(tweet[3]) and tweet[1] not in followers:
            # make sure we don't over follow, new limit is 5000
            # https://support.twitter.com/articles/66885?lang=en
            if len(followers_tuple) > 4001:
                cursor.execute(
                    "SELECT author_id FROM " +
                    DB_PREFIX +
                    "follows ORDER BY last_tweet_follow ASC LIMIT 1"
                )
                author_id = cursor.fetchone()[0]
                try:
                    api.destroy_friendship(id=author_id)
                except Exception as e:
                    # we may fail to destroy friendship as user was deleted
                    # etc. so we will still continue the process as usual
                    # status = 9
                    error = e
                    logger.error(str(error))
                    client.captureException()
		if error == None or error[0][0]['code'] == 34:
		    cursor.execute(
		        "DELETE FROM " +
		        DB_PREFIX + "follows WHERE author_id=%s LIMIT 1",
		        (author_id, )
		    )
		    db.commit()

            try:
                api.create_friendship(id=tweet[1], follow=True)
            except Exception as e:
                status = 9
                error = e
                logger.warning(str(error))
                client.captureException()
            else:
                try:
                    cursor.execute(
                        "REPLACE into " + DB_PREFIX +
                        "follows (author_id, last_tweet_follow) VALUES (%s, %s)",
                        (tweet[1], tweet[2].isoformat(" ").encode("ascii"))
                    )
                    db.commit()
                except Exception as e:
                    error = e
                    logger.error(str(error))
                    status = 9

        if needs_fav(tweet[3]):
            try:
                api.create_favorite(id=tweet[0])
            except Exception as e:
                status = 9
                error = e
                logger.warning(str(error))

        if status != 9:
            try:
                api.retweet(id=tweet[0])
                status = 1
		logger.warning('published tweet - %s' % tweet[0])
            except Exception as e:
                status = 9
                error = e
                logger.warning(str(error))
            '''
            else:
                fullTweet = api.get_status(tweet[0])
                if not fullTweet.retweeted:
                    print 'error'
                else:
                    print 'followed'
            '''

        if error is not None:
            try:
                code = error[0][0]['code']
            except (IndexError, KeyError):
                logger.warning(str(error))
            else:
                if code == 185:
                    time.sleep(60*15)  # we are over our limit, wait 15 minutes
                if code == 161:
                    time.sleep(60*60)  # we are over our limit, wait 60 minutes

        if status != 0:
            cursor.execute(
                "UPDATE " + DB_PREFIX +
                "retweets SET status=%s, error=%s WHERE tweet_id=%s",
                (status, error, tweet[0])
            )
            db.commit()
        else:
            print 'failed to retweet, no error'

        error = None  # avoid leak

        # retweet (tweet) limit is 2400 a day. or 4 actions a minute which
        # average at 35s
        time.sleep(randint(40, 45))

    if len(tweets) == 0:
        time.sleep(60)

if __name__ == '__main__':
    # default to eu
    tz = EU_TIME_ZONES
    lc = EU_LOCATIONS
    logging.basicConfig(
        filename="%sbasic.log" % DB_PREFIX, level=logging.WARNING,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

    # set Raven
    client = raven.Client(
        dsn='https://de6bc5b15d104a718820935456fe7b81:963ab45cb56f4ae3984f1cc845fc9aec@app.getsentry.com/50508',
        include_paths=['publisher.py']
    )

    # set up tweepy
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    while True:
        # Set DB connection
        db = MySQLdb.connect(host=DB_HOST,
                             user=DB_USER,
                             passwd=DB_PASSWORD,
                             db=DB_NAME,
                             use_unicode=True)

        db.row_factory = dict_factory
        cursor = db.cursor()
        fetch_new_tweets_from_db(tz, lc)
        db.close()
