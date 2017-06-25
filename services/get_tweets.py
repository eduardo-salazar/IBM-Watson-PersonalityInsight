from pymongo import MongoClient
import config
from bson.json_util import dumps
from .tweet import Tweet
class GetTweets:

    def __init__(self):
        #Connect To database
        client = MongoClient(config.db)
        self.db = client.geo_tweets

    def get_tweets_from(self, user):
        elements = self.db.tweets_en.find({'user.id': user})
        #Convert to Tweet Object
        result = []
        for doc in elements:
            result.append(Tweet(
            doc['id'],
            doc['user']['id'],
            doc['user']['name'],
            doc['user']['screen_name'],
            doc['text'],
            doc['created_at'],
            doc['lang']))
        return result
