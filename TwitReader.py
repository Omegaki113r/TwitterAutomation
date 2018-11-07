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

message="Hello World From My Twitter Bot #vuejs #programmer #coderlife #womenwhocode #java #python #javascript #csharp #cplusplus #django #webdeveloper #webdesign #ruby #sql #androiddeveloper #swift #php #html #css #html5 #reactjs #AngularJS #developer"
twitter.update_status(status=message)
print "tweeted: {}".format(message)