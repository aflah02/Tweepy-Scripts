import tweepy
import os
from helpers import *

consumer_key = os.environ['Tweepy_API_Key']
consumer_secret = os.environ['Tweepy_API_Secret_Key']
access_token = os.environ['Tweepy_Access_Token']
access_token_secret = os.environ['Tweepy_Secret_Access_Token']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
print(*get_friend_names(api, 'viditchess'))