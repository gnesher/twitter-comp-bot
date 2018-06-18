#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb
import sys
from local_settings import (DB_HOST, DB_USER, DB_PASSWORD, DB_NAME)

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

cursor.execute('SELECT tweet_id from retweets')
tweets = cursor.fetchall()
