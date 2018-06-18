import tweepy
from local_settings import (CONSUMER_KEY, ACCESS_KEY, CONSUMER_SECRET, ACCESS_SECRET)

if __name__ == '__main__':
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    list = []
    for member in tweepy.Cursor(api.list_members, 'HammerEmma', 'sharing-is-caring-group').items():
        list.append(member.id_str)
    thelist = open('userconstants.py', 'w')
    thelist.write("USER_LIST=%s\n" % list)

