import tweepy
import json


with open("twitterCredentials.json", "r") as read_file:
	credentials = json.load(read_file)
	read_file.close()
	print(credentials)
	

consumer_key = 'consumer key'
consumer_secret = 'consumer secrets'
access_token = 'access token'
access_token_secret = 'access token secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.me()
print (user.name)