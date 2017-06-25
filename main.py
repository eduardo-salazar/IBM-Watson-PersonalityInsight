import services.get_tweets.py
import services.get_personality.py

# Test user ID
# 2563976967
tweets_helper = GetTweets()
user_tweets = tweets_helper.get_tweets_from(2563976967)
