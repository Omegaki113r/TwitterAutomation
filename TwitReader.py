from twython import Twython
import threading

from auth import(consumer_key,consumer_secret,access_token,access_token_secret)

tweetsFile=open('C:/Users/OmegaKiller/Desktop/twitter/posts.txt','r')
tweets=tweetsFile.readlines()

for tweet in tweets:
    print tweet

i=0

twitter=Twython(consumer_key,consumer_secret,access_token,access_token_secret)


def postInTime(index):
    threading.Timer(18*60,postInTime).start()
    splitted=tweets[index].split(',')

    print splitted[0].rstrip()
    print splitted[1].rstrip()

    photo=open(splitted[1].rstrip(),"rb")
    response=twitter.upload_media(media=photo)
    twitter.update_status(status= splitted[0].rstrip(),media_ids=[response['media_id']])
    ++index

    if index>=len(tweets):
        i=0


postInTime(i)




