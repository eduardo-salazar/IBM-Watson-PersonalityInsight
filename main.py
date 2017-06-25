import services.get_tweets as tweetsHelper
import services.get_personality as pi
import time
# Test user ID
# 2563976967
tweets_helper = tweetsHelper.GetTweets()

users = []
users.append(2563976967)

timestr = time.strftime("%Y%m%d-%H%M%S")
fileName = "output/pi-"+timestr+".csv"

#Create Begining of file
f = open(fileName, 'w')
f.write("user,openness,conscientiousness,extraversion,agreeableness,neuroticism\n")  # python will convert \n to os.linesep
f.close()


for index, user in enumerate(users):
    user_tweets = tweets_helper.get_tweets_from(user)

    print("("+str(index+1)+" of "+str(len(users))+")Getting Personality Insight from user "+str(user))
    personalityInsight = pi.GetPersonalityInsight(user_tweets)
    user_pi = personalityInsight.call()

    traits = user_pi['personality']
    t_o=0
    t_c=0
    t_e=0
    t_a=0
    t_n=0
    for trait in traits:
        if(trait['trait_id']=="big5_openness"):
            t_o = trait['percentile']
        elif(trait['trait_id']=="big5_conscientiousness"):
            t_c = trait['percentile']
        elif(trait['trait_id']=="big5_extraversion"):
            t_e = trait['percentile']
        elif(trait['trait_id']=="big5_agreeableness"):
            t_a = trait['percentile']
        else:
            #big5_neuroticism
            t_n = trait['percentile']


    # Append to File Information
    with open(fileName, "a") as myfile:
        myfile.write(str(user)+","+str(t_o)+','+str(t_c)+','+str(t_e)+','+str(t_a)+','+str(t_n)+'\n')
