import services.get_tweets as tweetsHelper
import time
import traceback

tweets_helper = tweetsHelper.GetTweets()

# target_users = tweets_helper.get_target_users()

target_users = []
target_users.append(2457185017)


for index, user in enumerate(target_users):
    fileName = "tweets/"+str(user)+".csv"
    try:
        print("("+str(index+1)+" of "+str(len(target_users))+")Converting user "+str(user)+" to csv")
        #Create Begining of file
        f = open(fileName, 'w')
        f.write("tweetId,userId,userDescription,userName,userAlias,country_code,country_name,text,created_at\n")  # python will convert \n to os.linesep
        f.close()

        user_tweets = tweets_helper.get_tweets_from(user)
        print("information of tweet getted")
        count = 0
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
            print("("+str(++count)+" of "+str(len(user_tweets))+" saved)")
    except Exception as e:
        # Just print(e) is cleaner and more likely what you want,
        # but if you insist on printing message specifically whenever possible...
        traceback.print_exc()

        # Append to File Information
        with open(fileName, "a") as myfile:
            myfile.write(",,,,,,,,"+'\n')
