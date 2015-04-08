from TwitterSearch import *
import sys,ast

keywords = ast.literal_eval( sys.argv[1] )


wfile = open('twitter_output.txt', 'a')

try:
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.set_keywords(keywords) # let's define all words we would like to have a look for
    tso.set_language('en') # we want to see English tweets only
    tso.set_include_entities(False) # and don't give us all those entity information

    # it's about time to create a TwitterSearch object with our secret tokens
    ts = TwitterSearch(
        consumer_key = 'G0imX47NJvE8wHR7M6u4IPvx7',
        consumer_secret = 'B64E2PkubV27RZwYdPnKKeaiBOi6D8Nlh2XsqU52eHBcRcpbE2',
        access_token = '45286989-v6XORcMhQDQVAlB1AHv9TLxMyuWkmxJYNJ28TjwhI',
        access_token_secret = 'XilwoKHjaytzC91tKbnt0hkymwmoMXztVXKexHCSWTiPn'
     )

    
     # this is where the fun actually starts :)
    for tweet in ts.search_tweets_iterable(tso):
        if(tweet['retweet_count'] == 0):
            tweet_text = tweet['text'].encode('utf-8')
            printline =  tweet_text 
            wfile.write(printline)

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)