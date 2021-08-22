import tweepy
import os

consumer_key = os.environ['Tweepy_API_Key']
consumer_secret = os.environ['Tweepy_API_Secret_Key']
access_token = os.environ['Tweepy_Access_Token']
access_token_secret = os.environ['Tweepy_Access_Token']
print(consumer_key, consumer_secret, access_token, access_token_secret)
print(os.environ['OMDB_API_KEY'])
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
