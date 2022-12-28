# pylint: disable=unused-import
import tweepy
# import pandas as pd
import json
from datetime import datetime
import s3fs

access_key = "qMCwbaeaG484slcyr2FZZkm6T"
access_secret = "lYGm8zXrCtzT71q3o3i7PjUbMO5nB49dJhCffJXcIykirx4HzL"
consumer_key = "782057102-3WzrHI8opeMu0GbKYahF0zLbxdB3dLCXngoAIYbe"
consumer_secret = "qZXWrNIRK05I6xrYbCsS9jPLveL4rRywnTvW8EUTUkoI8"

# twitter authentication

auth = tweepy.OAuthHandler(access_key, access_secret)
auth.set_access_token(consumer_key, consumer_secret)

# creating api object

api = tweepy.API(auth)

tweets = api.user_timeline(screen_name='@elonmusk',
                           count=200,  # maximum number of tweets
                           include_rts=False,  # show retweets or not
                           tweet_mode='extended'
                           )
print(tweets)
