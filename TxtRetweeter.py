#import neccesary modules
import random
import tweepy
import time
import fileinput
#Access and Authenticate to twitter API
auth = tweepy.OAuthHandler("********", "*********")
auth.set_access_token("**********", "*************")
api = tweepy.API(auth)
#access,open, and read file
my_file = open('tweets.txt', 'r')
text = my_file.read()
my_file.close()
tweet = text.split('\n')
#ensures that there are no blank spaces in the .txt file
if tweet[-1]=='':
    tweet.pop()

def main():
    randomstat()
    
def randomstat():
    while True:
        #again opens and checks the file every time the function runs
        my_file = open('tweets.txt', 'r')
        text = my_file.read()
        my_file.close()
        tweet = text.split('\n')
        if tweet[-1]=='':
            tweet.pop()
        #sets and prints to terminal which tweet has been retweeted
        tweetchoice = random.choice(tweet)
        print(tweetchoice)
        #"Retweets" the tweet, more text can be add
        api.update_status(f"example comment {tweet}")
        #removes used tweet link from the .txt
        with open("tweets.txt", "r") as f:
            lines = f.readlines()
        with open("tweets.txt", "w") as f:
            for line in lines:
                if line.strip("\n") != statchoice:
                    f.write(line)
        #set timer to how often bot posts (set currently to every 12 hours)
        time.sleep(43200)
        
if __name__=="__main__":
    main()
