from pymongo import MongoClient
import config
from bson.json_util import dumps
from .tweet import Tweet
class GetTweets:

    def __init__(self):
        #Connect To database
        client = MongoClient(config.db)
        self.db = client.geo_tweets

    def count_target_users(self):
        return self.db.target_users.count()

    def get_target_users(self):
        elements = self.db.target_users.find()
        #Convert to Tweet Object
        result = []
        for doc in elements:
            result.append(doc['_id'])
        return result

    def get_tweets_from(self, user):
        elements = self.db.tweets_en.find({'user.id': user},{"user.id":1,"user.description":1,"user.name":1,"user.screen_name":1,"place.name":1,"place.full_name":1,"place.country_code":1,"place.country":1,"lang":1,"created_at":1,"id":1,"text":1})
        #Convert to Tweet Object
        result = []
        for doc in elements:
            result.append(Tweet(
            doc['id'],
            doc['user']['id'],
            doc['user']['name'],
            doc['user']['screen_name'],
            dos['user']['description'],
            doc['text'],
            doc['created_at'],
            doc['lang'],
            doc['place']['country_code'],
            doc['place']['country']))
        return result
