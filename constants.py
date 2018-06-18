#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from local_settings import DB_PREFIX
from userconstants import USER_LIST


QUERY = ["retweet win", "rt win", "giveaway rt", "giveaway retweet",
         "freebieFriday", "rttowin", "winitwednsday", "rt competition",
         "rt comp", "winitwednesday"]

TABLE_PREFIXES = ['gn', 'vd']

POSITIVE_KEYWORDS = {"win", "giveaway", "freebiefriday", "rttowin",
                     "winitwednsday", "comp", "competition",
                     "winitwednesday"}

FOLLOW_INDICATORS = {"follow", "flw", "following", "fllw"}

FAVOURITE_INDICATORS = {'fav', 'like'}

FILTER = 'SELECT tweet_id, author_id, tweet_time, tweet_text FROM ' + \
    DB_PREFIX + 'retweets WHERE status=0 ORDER BY RAND() LIMIT 1'

USER_STREAM = USER_LIST

BANNED_KEYWORDS = ["vote"]

IGNORED_USERS = []

IGNORED_KEYWORDS = ['pokemon', 'tpp', 'vgc09', 'quiz', '_rt_', 'justin', 'justinbieber',
                    'pokmon', 'render', 'csgo', 'minecraft', 'portrait', 'directioner',
                    'fifa', 'fut', 'smite', 'totw', 'onedirection', 'nba', 'coins', 'help',
                    'tattoo', 'tattoos', 'beta', 'bo3', 'dlc', 'header', 'bra', 'nothing',
                    'canada', 'twitch', 'notifications', 'tix', 'csgoshuffle', 'getmeonharmony',
                    'betabo3', 'bo3beta', 'bo3betacode', 'csgojackpot', '5sos',
                    'cards', 'win followers', 'topps', 'therapy', 'keyrings', 'vip booth',
                    'ive entered', 'i want', 'solo dm', 'show proof', 'win follows', 'are active',
                    "deserve to win", "I wanna win", "who would win in a", 'cs_giveaways',
                    'dm giveaway', "turn on notifications", 'subscribe to my channel', 'p2000',
                    'vote', ' trump ', 'bernie', 'ted cruz', 'favorite if u think', 'tag mates',
                    'favorite if', 'win or lose', 'who will win', '100k', '200k', '50k', 'heatran',
                    'deserves to win', 'i wanna win', 'one vote', 'account', 'toty', 'notification',
                    'subscribe', 'youtube', 'coin', 'ak47', 'dm with', 'united states only', 'us only',
                    'madden', 'sub at', 'congrats', 'turn on our', '500k', '10k psn', 'turn notif',
                    'tag 2', 'tag 3', 'to win cal', 'free bet', 'bar tab', 'like lose', 'awp',
                    'who would win', 'who will win', ' bet ', ' bets ', 'free follows', 'flip knife',
                    'stay active', 'dms giveaway', 'dm giveaway', 'rt if you think', 'doppler',
                    'win the league', 'esurancesweepstakes', 'awp', 'like if', 'glock', 'going to win',
                    'umg credit', 'skins', 'if you want this', 'pangako ng hustisya', 'otwol', ' gfx ',
                    'minecon', 'dm solo', 'mew code', 'now closed', 'retweet if you agree', 'flip knife',
                    'tigertooth knife', 'knife stattrak', 'butterfly knife', 'graphics giveaway',
                    'who do you think will win', 'gonna win', 'congratulate', 'do you think', 'congratulations',
                    'more followers', 'will check', 'icon giveaway', 'thumbnail giveaway', 'diancie',
                    'win at our website', 'acc giveaway', 'retweet if you think', 'lifetime', 'if the',
                    'mewtwo', 'pakistan', 'free followers', '1 rt =', 'enti', 'making maths fun', 'bangladesh',
                    'win the final', 'barca', 'want the girls to win', 'harmonizers', 'must be active',
                    'win or draw', ' dms', 'your pick to win', 'we win', 'you want us to win',
                    'entei', 'ambipom', 'who would you', 'we can win this', 'katy perry', 'bestfanarmy',
                    'pidove', 'trying to win', 'voting', 'beliebers', 'click to enter', 'share your',
                    'enter here', 'tag a friend', 'starmie', 'find out how', 'bayonet', 'not to win',
                    'tell us', 'ul giveaway', 'fb comp', 'kingdra', 'draftking', 'answer', 'click here',
                    'tag a friend', 'banner', 'guess', 'psc giveaway', 'share a pic', 'wallpaper giveaway',
		    'gold giveaway', 'full access', 'skin giveaway', 'texture pack', 'want her to win',
		    'want him to win', ]

EU_LOCATIONS = ['brighton', 'united kingdom', 'england, united kingdom', 'south east, england',
                'liverpool, england', 'london, england', 'uk', 'bristol', 'cardiff, wales',
                'dublin,ireland', 'portsmouth, uk', 'england', 'west midlands, england',
                'manchester & edinburgh | uk', 'united kingdom/ireland ', 'surrey', 'high wycombe, england',
                'great britain ', 'great britain', 'london', 'southampton, uk', 'north east, england',
                'royal tunbridge wells, england', 'dublin city, ireland', 'south wales', 'yorkshire, england, uk',
                'birmingham, england', 'uk based business only.', 'united kindom', 'yorkshire, uk',
                'worldwide', 'norwich, england', 'wales, united kingdom', 'london & europe',
                'gloucestershire, uk', 'derbyshire, england', 'scotland', 'hampshire | surrey',
                'leeds', 'gloucestershire, uk', 'manchester', 'manchester, england', 'yorkshire, england',
                'kingstone, england', 'buxton, england', 'west bromwich', 'somerset, uk', 'yorkshire uk',
                'scotland, united kingdom', 'england, uk', 'soho, london', 'sheffield, england',
                'sheffield, uk', 'northern ireland', 'northern ireland, united kingdom', 'yorkshire',
                'newcastle upon tyne, england', 'newcastle', 'london, uk', 'london, ec1v 4pw', 'york, united kingdom'
                'london | worldwide', 'london uk', 'london // essex', 'london (uk)', 'liverpool',
                'lancashire', 'ireland', 'hull, england', 'greater london.', 'exeter', 'essex',
                'essex ', 'edinburgh', 'dublin-cork-regional & global', 'dublin, ireland', 'dublin',
                'bishopbriggs, scotland', 'birmingham, uk', 'northwich', 'ｕｋ', 'york, north yorkshire',
                'york', 'wythenshawe, manchester', 'wymondham, norfolk, england', 'wiltshire', 'west midlands, uk',
                'wales', 'united kingdom', 'stoke-on-trent/nottingham ', 'shotton', 'nottingham', 'north west, england',
                'milton keynes, england', 'manchester, uk', 'manchester / cheshire', 'manchester',
                'london | melbourne', ]

EU_TIME_ZONES = ['london', 'edinburgh', 'dublin', 'amsterdam', 'lisbon',
                 'casablanca', 'utc', 'europe/london', 'dublin & london', ]
