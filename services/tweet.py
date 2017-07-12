from datetime import datetime
class Tweet:
    def __init__(self, tweetId,userId, name, alias,description, text,created_at,lang,country_code,country_name):
        # print(str(userId))
        self.__userId = userId
        # print(str(tweetId))
        self.__tweetId = tweetId,
        # print(name)
        self.__name = name
        # print(alias)
        self.__alias = alias
        # print(text)
        self.__text = text
        # print(description)
        self.__description = description
        # print(str(created_at))
        self.__created_at = created_at
        # print(lang)
        self.__lang = lang
        # print(country_code)
        self.__country_code = country_code
        # print(country_name)
        self.__country_name = country_name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value

    @property
    def userId(self):
        return self.__userId

    @userId.setter
    def userId(self,value):
        self.__userId = value

    @property
    def tweetId(self):
        return self.__tweetId

    @tweetId.setter
    def tweetId(self,value):
        self.__tweetId = value

    @property
    def alias(self):
        return self.__alias

    @alias.setter
    def alias(self,value):
        self.__alias = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self,value):
        self.__description = value

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self,value):
        self.__text = value

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self,value):
        self.__created_at = value

    @property
    def lang(self):
        return self.__lang

    @lang.setter
    def lang(self,value):
        self.__lang = value

    @property
    def country_code(self):
        return self.__country_code

    @country_code.setter
    def country_code(self,value):
        self.__country_code = value

    @property
    def country_name(self):
        return self.__country_name

    @country_name.setter
    def country_name(self,value):
        self.__country_name = value

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
