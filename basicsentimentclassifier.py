from typing import Text
import tweepy
import os
from textblob import TextBlob

consumer_key = os.environ['Tweepy_API_Key']
consumer_secret = os.environ['Tweepy_API_Secret_Key']
access_token = os.environ['Tweepy_Access_Token']
access_token_secret = os.environ['Tweepy_Secret_Access_Token']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
username = input('Enter userid for person whose tweets we need to analyze? ')
public_tweets = api.search(username)
ls_score = []
ls_tweet = []
for tweet in public_tweets:
    ls_tweet.append(tweet.text)
    ls_score.append(TextBlob(tweet.text).sentiment)
