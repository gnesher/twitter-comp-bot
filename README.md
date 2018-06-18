# twitter-comp-bot
A database driven Twitter competition bot written in Python

# a little background
I've been running a twitter competition bot in the UK for about 3 years.
The bot has finally been blocked by Twitter and I've already left the UK last year so I thought it's time to share the code as it's the most advanced script I've seen so far
This doesn't mean the code is written well - as it was an experiment at playing with Python. But it does work, and has provided hundreds of prizes over it's lifetime.

# I obviously take no responsibility for any problems that may be caused by running this code.
My account was eventually locked (though it took 3 years)

# Set up instructions
This is just a rough guide, some changes might be required.
1. Set up a database and use the create_sql_tables to create the tables.
2. Run pip install -r requirements.txt to set up dependencies (Python using pip)
3. Set up a twitter dev account and insert required credentials into local_settings.py (including db data)
4. You need to run 2 processes, new_consumer.py to populate the db with competition tweets and publisher to retweet / enter the competition
5. There's a whole bunch of other helper files here, a lot of them were used during development to clean db, reset account etc.

