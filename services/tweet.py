from datetime import datetime
class Tweet:
    def __init__(self, tweetId,userId, name, alias, text,created_at,lang):
        self.userId = userId
        self.tweetId = tweetId,
        self.name = name
        self.alias = alias
        self.text = text
        self.created_at = created_at
        self.lang = lang

    def name(self):
        return self.name

    def userId(self):
        return self.userId

    def tweetId(self):
        return self.tweetId

    def alias(self):
        return self.alias

    def text(self):
        return self.text

    def created_at(self):
        return self.created_at

    def lang(self):
        return self.lang


    def toJSON(tweet):
        return {
            'userid': str(tweet.userId),
            'id': str(tweet.tweetId),
            'sourceid': 'python-twitter',
            'contenttype': 'text/plain',
            'language': tweet.lang,
            'content': tweet.text,
            'created': tweet.created_at.strftime('%s')
        }
