#Import the necessary methods from tweepy library

from __future__ import absolute_import, print_function

import tweepy
import json
import sys, ast



#Variables that contains the user credentials to access Twitter API 
consumer_key = 'G0imX47NJvE8wHR7M6u4IPvx7'
consumer_secret = 'B64E2PkubV27RZwYdPnKKeaiBOi6D8Nlh2XsqU52eHBcRcpbE2'
access_token = '45286989-v6XORcMhQDQVAlB1AHv9TLxMyuWkmxJYNJ28TjwhI'
access_token_secret = 'XilwoKHjaytzC91tKbnt0hkymwmoMXztVXKexHCSWTiPn'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


for tweet in tweepy.Cursor(api.search,
                           q="FastFurious7",
                           count=100,
                           result_type="recent",
                           include_entities=False).items():
    json_string = tweet._json
    json_text = json.dumps(json_string)
    print(json_text)