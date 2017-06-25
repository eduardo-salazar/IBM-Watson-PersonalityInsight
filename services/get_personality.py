import sys
import requests
import json
import twitter
import config
from .tweet import Tweet

# This class Connects to Watson API and saves into file
# the personality Insight of the user tweets
class GetPersonalityInsight:
    # helper to transfor tweet into correct format for api
    def convert_tweet_to_pi_content_item(tweet):
        # Format of Watson PI
        # return {
        #     'userid': str(s.user.id),
        #     'id': str(s.id),
        #     'sourceid': 'python-twitter',
        #     'contenttype': 'text/plain',
        #     'language': s.lang,
        #     'content': s.text,
        #     'created': s.created_at_in_seconds,
        #     'reply': (s.in_reply_to_status_id == None),
        #     'forward': False
        # }
        return {
            "userid": str(tweet.userId),
            "id": str(tweet.tweetId),
            "sourceid": "python-twitter",
            "contenttype": "text/plain",
            "language": tweet.lang,
            "content": tweet.text,
            "created": tweet.created_at
        }

    def __init__(self,tweets):
        self.tweets = tweets

    def call(self):
        pi_content_items_array = []
        for result in self.tweets:
            pi_content_items_array.append(result.toJSON())
        pi_content_items = {'contentItems': pi_content_items_array}
        r = requests.post(config.pi_url + '/v3/profile?version=2016-10-20&consumption_preferences=true&raw_scores=true',
                          auth=(config.pi_username, config.pi_password),
                          headers={
                              'content-type': 'application/json',
                              'accept': 'application/json'
                          },
                          data=json.dumps(pi_content_items)
                          )

        print("Profile Request sent. Status code: %d, content-type: %s" % (r.status_code, r.headers['content-type']))
        response = json.loads(r.text)
        return response

        # Format output in csv file
