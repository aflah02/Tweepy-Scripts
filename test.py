import tweepy
import os
import pandas as pd
import numpy as np

consumer_key = os.environ['Tweepy_API_Key']
consumer_secret = os.environ['Tweepy_API_Secret_Key']
access_token = os.environ['Tweepy_Access_Token']
access_token_secret = os.environ['Tweepy_Secret_Access_Token']
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth, wait_on_rate_limit_notify =True, wait_on_rate_limit=True)
df = pd.read_csv('abc.tsv', sep='\t', names=['tweet_id'])

ls_tweets = df['tweet_id'].to_numpy(dtype=str)
ls2 = []
for i in range(len(ls_tweets)):
    ls2.append(str(ls_tweets[i]))
tweetFetched = api.statuses_lookup([ls2[0], ls2[1]])
# print(tweetFetched)
with open('file.txt', 'w', encoding='utf-8') as f:
    for item in tweetFetched:
        f.write("%s\n" % item.text)