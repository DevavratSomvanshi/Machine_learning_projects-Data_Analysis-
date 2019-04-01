# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 21:11:19 2019

@author: nEW u
"""

import tweepy
from textblob import TextBlob
import csv

consumer_key="bq9ipYGm4uc2fs89KsLY3UIJh"
consumer_secret="l5QNafi0yiiMxSDO3yGmM0nccewj0rOzDaAPZRzDoWHyOJy2y1"

access_token="3172411831-DeevjQvayL2qFLgxMC8POFh9atPZVMcOvDA5Pgg"
access_token_secret="xFRbsOQ3yEMiLlj9fpKUEFHMDBqDABKmlON9kbtgRDvQH"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search('modi')


a=[]

for tweets in public_tweets:
    a.append(tweets.text)
    print(tweets.text)
    wiki=TextBlob(tweets.text)
    print(wiki.sentiment)
    

 
myFile = open('sentiment.csv', 'w')  
with myFile:  
   writer = csv.writer(myFile)
   writer.writerows([a])