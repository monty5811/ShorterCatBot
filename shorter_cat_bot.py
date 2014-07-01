import os
import re
import time
import json
import tweepy

# read in the WSC
with open('ShorterCat.json', 'r') as f:
    qAndA = json.load(f)

# login to twitter api
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# read in progress:
with open('progress', 'a+') as f:
    try:
        i = int(f.read()) % 107
    except Exception, e:
        print 'No progress file - starting from Q1.'
        i = 0

# get Q and A:
Q = 'Q'+str(i+1)+':' + qAndA['Q'+str(i+1)]
A = 'A'+str(i+1)+':' + qAndA['A'+str(i+1)]

# ensure answers fit inside a tweet
if len(A) > 140:
    counter = 0
    answer_tweets = ['']
    # split into several tweets:
    for x in A.split(' '):
        if len(answer_tweets[counter]) + len(x) < 138:
            answer_tweets[counter] += x
            answer_tweets[counter] += ' '
        else:
            answer_tweets.append('A'+str(i+1)+':')
            counter += 1
            answer_tweets[counter] += x
            answer_tweets[counter] += ' '
    answer_tweets[counter] = answer_tweets[counter].replace(' ,', '')
else:
    answer_tweets = [A]

# send tweets
api.update_status(Q.strip())
time.sleep(1)
for tweet in answer_tweets:
    api.update_status(tweet.strip())
    time.sleep(1)

# update progress
i += 1
with open('progress', 'w') as f:
    f.write(str(i))
