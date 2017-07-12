from datetime import datetime
class Tweet:
    def __init__(self, tweetId,userId, name, alias,description, text,created_at,lang,country_code,country_name):
        self.userId = userId
        self.tweetId = tweetId,
        self.name = name
        self.alias = alias
        self.text = text
        self.description = description
        self.created_at = created_at
        self.lang = lang
        self.country_code = country_code
        self.country_name = country_name

    @property
    def name(self):
        return self.name

    @property
    def userId(self):
        return self.userId

    @property
    def created_at(self):
        return self.created_at

    @property
    def tweetId(self):
        return self.tweetId

    @property
    def alias(self):
        return self.alias

    @property
    def description(self):
        return self.description

    @description.setter
    def description(self,value):
        self.description = value

    @property
    def text(self):
        return self.text

    @text.setter
    def text(self,value):
        self.text = value

    @property
    def created_at(self):
        return self.created_at

    @property
    def lang(self):
        return self.lang

    @property
    def country_code(self):
        return self.country_code

    @property
    def country_name(self):
        return self.country_name

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
