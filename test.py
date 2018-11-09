import tweepy
import json

# Read the credentials needed to authenticate with the api from a JSON file so the credentials are not published on GitHub
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

def mainFunction():
	search = "Keyword"
	numberOfTweets = "Number of tweets I am interacting with"
	for tweet in tweepy.Cursor(api.search, search).items(numberOfTweets):
		try:
			tweet.favorite()
			print('Favorited the tweet')
		except tweepy.TweepError as e:
			print(e.reason)
		except StopIteration:
			break