import tweepy
import configparser
import pandas as pd
import csv

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Put your Bearer Token in the parenthesis below
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAAFOVlgEAAAAAUlvX%2B9YoFl%2BPkxEjysaluPxaDEc%3DYNggIb56fO8n4uRRUXkXfIiQyOBAp5HC332SbLamXbWOnE2g78')



# Get tweets that contain the hashtag #petday
# -is:retweet means I don't want retweets
# lang:en is asking for the tweets to be in english

tweets = tweepy.Paginator(client.search_recent_tweets, query='latest -is:retweet lang:te', max_results=100).flatten(limit=5000)

"""
What context_annotations are: 
https://developer.twitter.com/en/docs/twitter-api/annotations/overview
"""
columns = ['Tweet']
data = []
for tweet in tweets:
    data.append([tweet.text])

df = pd.DataFrame(data, columns=columns)

df.to_csv('tweets.csv')


