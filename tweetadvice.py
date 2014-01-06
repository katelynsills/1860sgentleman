import twitter
import random
import os
import re

#open the source file

guide = open('gentsguide.txt', 'r').read()

#divide the source file up into tweetable sentences
guide = re.split('\.|\?', guide)
print guide

#pick a random quote
max = len(guide)
length = 200
while length > 140 or length < 1:
	quote = guide[random.randint(0,max-1)].strip()
	length = len(quote)

print quote
print len(quote)


api = twitter.Api(consumer_key=os.environ['T_CONSUMER_KEY'],
				  consumer_secret=os.environ['T_CONSUMER_SECRET'],
				  access_token_key=os.environ['T_ACCESS_TOKEN_KEY'],
				  access_token_secret=os.environ['T_ACCESS_TOKEN_SECRET'])
api.PostUpdates(quote)



#attempt to shorten it?
#post a random quote (4 times a day?)
#delete the random quote from the source file?

