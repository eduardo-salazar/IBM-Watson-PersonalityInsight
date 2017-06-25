import sys
import requests
import json
import twitter
import config

# This class Connects to Watson API and saves into file
# the personality Insight of the user tweets
class GetPersonalityInsight:
    # helper to transfor tweet into correct format for api
    def convert_tweet_to_pi_content_item(s):
        # Format of Watson PI
        return {
            'userid': str(s.user.id),
            'id': str(s.id),
            'sourceid': 'python-twitter',
            'contenttype': 'text/plain',
            'language': s.lang,
            'content': s.text,
            'created': s.created_at_in_seconds,
            'reply': (s.in_reply_to_status_id == None),
            'forward': False
        }

    def __init__(self,tweets):
        self.tweets = tweets

    def call(self):
        pi_content_items_array = map(convert_tweet_to_pi_content_item, self.tweets)
        pi_content_items = {'contentItems': pi_content_items_array}

        r = requests.post(config.pi_url + '/v3/profile',
                          auth=(config.pi_username, config.pi_password),
                          headers={
                              'content-type': 'application/json',
                              'accept': 'application/json'
                          },
                          data=json.dumps(pi_content_items)
                          )

        print("Profile Request sent. Status code: %d, content-type: %s" % (r.status_code, r.headers['content-type']))
        print json.loads(r.text)

        # Format output in csv file
