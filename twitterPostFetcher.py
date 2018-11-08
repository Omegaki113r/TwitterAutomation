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

result=twitter.show_user(screen_name='Omegaki113r')
print result
tweet=twitter.show_status(id=12)
print tweet