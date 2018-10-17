import tweepy
from sys import argv 
from api import *
from time import sleep

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.me()
""" search = "ecell_iiithyd"
number = "50"

for tweet in tweepy.Cursor(api.search, search).items(number):
    try:
        tweet.retweet()
        print('retweeted') 
        print(tweet.text)

    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
    except KeyboardInterrupt:
        print('Tweeting done for the day')
        break """

print(user)