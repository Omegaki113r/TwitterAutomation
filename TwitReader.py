from twython import Twython
import threading

from auth import(consumer_key,consumer_secret,access_token,access_token_secret)

numberOfPosts=0
i=0
twitter=Twython(consumer_key,consumer_secret,access_token,access_token_secret)


tweetsFile = open('C:/Users/OmegaKiller/Desktop/twitter/posts.txt', 'r')
tweets = tweetsFile.readlines()

numberOfPosts = len(tweets)
tweetsFile.close()



def postInTime():
    global i

    print i

    threading.Timer(2*60,postInTime).start()
    splitted=tweets[i].split(',')

    print splitted[0].rstrip()
    print splitted[1].rstrip()

    photo=open(splitted[1].rstrip(),"rb")
    response=twitter.upload_media(media=photo)
    twitter.update_status(status= splitted[0].rstrip(),media_ids=[response['media_id']])

    i=i+1

    print i

    if i>=len(tweets):
        i=0

        print i
    print i



postInTime()




