from pymongo import MongoClient
import config
class GetTweets:

    def __init__(self):
        #Connect To database
        client = MongoClient(config.db)
        self.db = client.geo_tweets

    def get_tweets_from(self, user):
        self.db.tweets_en.find({'user.id': user})
