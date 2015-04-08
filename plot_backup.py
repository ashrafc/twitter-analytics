import json
import pandas as pd
import matplotlib.pyplot as plt
import pylab
import unirest
from collections import Counter
import csv
from wordcloud import WordCloud, STOPWORDS
from os import path
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import csv
import tweepy

tweets_data = []
sentiment_type = []
sentiment_score = []
sentiment_result_code =[]
sentiment_result_msg =[]

tweets_file = open("print_tweets.txt", "r")
for line in tweets_file:
    try:
		tweet = json.loads(line)
		tweets_data.append(tweet)
    except:
       	continue

print len(tweets_data)

def get_data(tweets_data):
	f = open("tweet_data.csv", 'wt')
	writer = csv.writer(f)
	writer.writerow( ('Tweet-Text', 'Tweet-Lang', 'Tweet-country', 'sentiment_type', 'sentiment_score', 'sentiment_result_code', 'sentiment_result_msg') )
	for tweets in tweets_data:
		tweet_text = tweets['text'].encode('ascii', 'ignore')
		response = unirest.post("https://twinword-sentiment-analysis.p.mashape.com/analyze/",
			headers={"X-Mashape-Key": "sGskCbyg1kmshjbTFyTlZCsjHv4vp1MGPV8jsnB1Qfk2Y8Q5Nt",
			"Content-Type": "application/x-www-form-urlencoded",
			"Accept": "application/json"
			},params={"text": tweet_text})
		response_body = response.body
		response_type = response_body['type'].encode('ascii', 'ignore')
		print response_type
		response_score = response_body['score']
		response_result_code = response_body['result_code'].encode('ascii', 'ignore')
		response_result_msg = response_body['result_msg'].encode('ascii', 'ignore')
		sentiment_type.append(response_type)
		sentiment_score.append(response_score)
		sentiment_result_code.append(response_result_code)
		sentiment_result_msg.append(response_result_msg)
		tweet_lang = tweets['lang'].encode('ascii', 'ignore')
		tweet_country = tweets['place']['country'].encode('ascii', 'ignore') if tweets['place'] != None else None
		writer.writerow((tweet_text, tweet_lang, tweet_country, response_type, response_score, response_result_code, response_result_msg) )
	f.close()
	pass
'''
def get_twitter_data():
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
	    tweet = json.loads(json_text)
	    tweets_data.append(tweet)
	    if len(tweets_data) == 100:
	    	get_data(tweets_data)

get_twitter_data()
'''

def plot(tweets):

	tweets_by_sentiment_type = tweets['sentiment_type'].value_counts()
	#print(tweets_by_sentiment_type)

	fig, ax = plt.subplots()
	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Sentiment Type', fontsize=15)
	ax.set_ylabel('Number of tweets' , fontsize=15)
	ax.set_title('Sentiment Type Count', fontsize=15, fontweight='bold')
	tweets_by_sentiment_type[:5].plot(ax=ax, kind='bar', color='black')	

	tweets_by_lang = tweets['Tweet-Lang'].value_counts()
	#print(tweets_by_lang)

	fig, ax = plt.subplots()
	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Languages', fontsize=15)
	ax.set_ylabel('Number of tweets' , fontsize=15)
	ax.set_title('Top 5 languages', fontsize=15, fontweight='bold')
	tweets_by_lang[:5].plot(ax=ax, kind='bar', color='red')

	tweets_by_country = tweets['Tweet-country'].value_counts()

	fig, ax = plt.subplots()
	ax.tick_params(axis='x', labelsize=15)
	ax.tick_params(axis='y', labelsize=10)
	ax.set_xlabel('Countries', fontsize=15)
	ax.set_ylabel('Number of tweets' , fontsize=15)
	ax.set_title('Top 5 countries', fontsize=15, fontweight='bold')
	tweets_by_country[:5].plot(ax=ax, kind='bar', color='blue')
	pylab.show()

tweets = pd.read_csv('tweet_data.csv')
pd.set_option('display.max_columns', None)
plot(tweets)
