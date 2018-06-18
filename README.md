# twitter-comp-bot
A database driven Twitter competition bot written in Python

# a little background
I've been running a twitter competition bot in the UK for about 3 years.
The account has finally been blocked by Twitter and I've already left the UK last year so I thought I'd the code I've written so far.
While it's not the cleanest code out there the bot was the most successful I've seen (and I've compared it to other solutions avilable in Github).

# I take no responsibility for any problems which may be caused by running this code.
My account was eventually locked (though it took 3 years).

# Set up instructions
This is just a rough guide, some changes might be required.
1. Set up a database and use the create_sql_tables to create the tables.
2. Run pip install -r requirements.txt to set up dependencies (Python using pip)
3. Set up a twitter dev account and insert required credentials into local_settings.py (including db data)
4. You need to run 2 processes, new_consumer.py to populate the db with competition tweets and publisher to retweet / enter the competition
5. There's a whole bunch of other helper files here, a lot of them were used during development to clean db, reset account etc.

