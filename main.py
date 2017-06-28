import services.get_tweets as tweetsHelper
import services.get_personality as pi
import time
# Test user ID
# 2563976967
tweets_helper = tweetsHelper.GetTweets()

#Pro
target_users = tweets_helper.get_target_users()

#Test
# target_users = []
# target_users.append(2563976967)

print("Total users are")
print(str(len(target_users)))

timestr = time.strftime("%Y%m%d-%H%M%S")
fileName = "output/pi-"+timestr+".csv"

#Create Begining of file
f = open(fileName, 'w')
f.write("user,tweets,openness,conscientiousness,extraversion,agreeableness,neuroticism\n")  # python will convert \n to os.linesep
f.close()


for index, user in enumerate(target_users):
    if(index + 1 > 1378):
        try:
            print("("+str(index+1)+" of "+str(len(target_users))+")Analysis of user "+str(user))
            user_tweets = tweets_helper.get_tweets_from(user)

            print("Trying to get Personality Insight From IBM Watson")
            personalityInsight = pi.GetPersonalityInsight(user_tweets)
            user_pi = personalityInsight.call()

            print("Reading Response of IBM Watson")
            print(user_pi)
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

            print("Saving user result ")
            # Append to File Information
            with open(fileName, "a") as myfile:
                myfile.write(str(user)+","+str(len(user_tweets))+","+str(t_o)+','+str(t_c)+','+str(t_e)+','+str(t_a)+','+str(t_n)+'\n')
        except:
            # Append to File Information
            with open(fileName, "a") as myfile:
                myfile.write(str(user)+","+str(len(user_tweets))+",,,,,"+'\n')
