import tweepy
from sys import argv 
from api import *
from time import sleep

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

user = api.me()
number = "50"

""" This function retweets for a given keyword """
def retweet(keyword):
    for tweet in tweepy.Cursor(api.search, keyword).items(number):
        try:
            tweet.retweet()
            print('retweeted') 
            print(tweet.text)

        except tweepy.TweepError as e:
            print(str(e.message))
        except StopIteration:
            break
        except KeyboardInterrupt:
            print('Tweeting done for the day')
            break


""" This function returns data about a tweet such as text and basic info about that person """
def searching(keyword):
    for tweet in tweepy.Cursor(api.search, keyword).items(1):
        try:
            texty =  tweet.text
            author = tweet.author
            name = author.name
            screen_name = author.screen_name
            followers = author.followers_count
            print("Name: "+ name)
            print("Screen Name : " + screen_name)
            print("Followers : " + str(followers))
            print("Text : " +texty)
            print("Do we follow : " + str(author.following))
            
        except tweepy.TweepError as e:
            print(str(e.message))
        except StopIteration:
            break
        except KeyboardInterrupt:
            print('Searched done for the day')
            break

if __name__ == '__main__':
    keyword =  raw_input("Enter keyword for retweet ")
    # retweet(keyword)
    searching(keyword)

