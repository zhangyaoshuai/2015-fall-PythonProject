import tweepy
from tweepy import OAuthHandler
import json
consumer_key='5y3XhbDQwMXHMV4P9r6GRU5yD'
consumer_secret='EdJ6Uhk8c4OAejqT4QqtaheuSzQwxpUY8z6iCbtIkU24r4qOqh'
access_token='505858397-c74YbKAzDnf0kUJ8eyxjDr3irLKcLk8Xi2auT1QK'
access_secret='5OQyfK2T4OOoT27QhJdVbIbrxWeirsCsbjsMz1QDGg5NW'
auth=OAuthHandler('5y3XhbDQwMXHMV4P9r6GRU5yD','EdJ6Uhk8c4OAejqT4QqtaheuSzQwxpUY8z6iCbtIkU24r4qOqh')
auth.set_access_token('505858397-c74YbKAzDnf0kUJ8eyxjDr3irLKcLk8Xi2auT1QK','5OQyfK2T4OOoT27QhJdVbIbrxWeirsCsbjsMz1QDGg5NW')
api=tweepy.API(auth)
def process_or_store(tweet):
    print(json.dumps(tweet))
for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)
    print('\n')
    print(' ')
    print('\n')
