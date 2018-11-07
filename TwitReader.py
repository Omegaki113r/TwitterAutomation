from twython import Twython

from auth import(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

twitter=Twython(consumer_key,
                consumer_secret,
                access_token,
                access_token_secret)

photo=open("C:/Users/OmegaKiller/Desktop/twitter/3fc333d34872f31113e0f21d5a896927.png","rb")
response=twitter.upload_media(media=photo)
twitter.update_status(status="This photo is uploaded by a bot",media_ids=[response['media_id']])
