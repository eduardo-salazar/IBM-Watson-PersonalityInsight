import services.get_tweets as tweetsHelper
import time

tweets_helper = tweetsHelper.GetTweets()

target_users = tweets_helper.get_target_users()

for index, user in enumerate(target_users):
    try:
        fileName = "tweets/"+user+".csv"
        print("("+str(index+1)+" of "+str(len(target_users))+")Converting user "+str(user)+" to csv")

        #Create Begining of file
        f = open(fileName, 'w')
        f.write("tweetId,userId,userDescription,userName,userAlias,country_code,country_name,text,created_at\n")  # python will convert \n to os.linesep
        f.close()

        user_tweets = tweets_helper.get_tweets_from(user)
        for result in user_tweets:
            # Append to File Information
            with open(fileName, "a") as myfile:
                myfile.write(str(result.tweetId)+","
                +str(user)+","
                +str(result.description)+','
                +str(result.name)+','
                +str(result.alias)+','
                +str(result.country_code)+','
                +str(result.country_name)+','
                +str(result.text)+','
                +str(result.created_at)
                +'\n')
    except:
        # Append to File Information
        with open(fileName, "a") as myfile:
            myfile.write(",,,,,,,,"+'\n')
