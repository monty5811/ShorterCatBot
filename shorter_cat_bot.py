import os
import re
import time
import tweepy

# read in the WSC
with open('ShorterCat.txt', 'r') as f:
    qAndA = list(f)

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

# split into Q and A:
q = qAndA[i]
findA = re.findall(u'A[0-9]', q)
q = q[0:q.find(findA[0])]
A = qAndA[i]
A = A[A.find(findA[0]):-1]

# ensure answers fit inside a tweet
if len(A) > 140:
    counter = 0
    answer_tweets = ['']
    # split into several tweets:
    for x in A.split(', '):
        if len(answer_tweets[counter]) + len(x) < 138:
            answer_tweets[counter] += x
            answer_tweets[counter] += ', '
        else:
            answer_tweets.append(A[0:A.find(':') + 2])
            counter += 1
            answer_tweets[counter] += x
            answer_tweets[counter] += ', '
    answer_tweets[counter] = answer_tweets[counter].replace(' ,', '')
else:
    answer_tweets = [A]

# send tweets
api.update_status(q.strip())
time.sleep(1)
for tweet in answer_tweets:
    api.update_status(tweet.strip())
    time.sleep(1)

# update progress
i += 1
with open('progress', 'w') as f:
    f.write(str(i))
