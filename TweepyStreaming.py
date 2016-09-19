import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json

consumer_key='5y3XhbDQwMXHMV4P9r6GRU5yD'
consumer_secret='EdJ6Uhk8c4OAejqT4QqtaheuSzQwxpUY8z6iCbtIkU24r4qOqh'
access_token='505858397-c74YbKAzDnf0kUJ8eyxjDr3irLKcLk8Xi2auT1QK'
access_secret='5OQyfK2T4OOoT27QhJdVbIbrxWeirsCsbjsMz1QDGg5NW'
auth=OAuthHandler('5y3XhbDQwMXHMV4P9r6GRU5yD','EdJ6Uhk8c4OAejqT4QqtaheuSzQwxpUY8z6iCbtIkU24r4qOqh')
auth.set_access_token('505858397-c74YbKAzDnf0kUJ8eyxjDr3irLKcLk8Xi2auT1QK','5OQyfK2T4OOoT27QhJdVbIbrxWeirsCsbjsMz1QDGg5NW')
api=tweepy.API(auth)

class MyListener(StreamListener):
    
    def on_data(self, data):
        
        try:
            with open('football.json', 'a') as f:
              
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['football'])
