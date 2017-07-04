class CleanTweet:
    def __init__(self, tweets):
        self.tweets = tweets

    def clean(self,msg_tweet):
        #Here is the clean of a single tweet

    def call(self):
        for(tweet in self.tweets):
            tweet.text = self.clean(tweet.text)
        return self.tweets
