import tweepy
import json

# Read the credentials needed to authenticate with the api from a JSON file so the credentials are not published on GitHub
def getCredentials(fileLocation):
	with open(fileLocation, "r") as read_file:
		credentials = json.load(read_file)
		read_file.close()
	return credentials
	
def login_api():
	consumer_key = getCredentials("twitterCredentials.json")['consumer_key']
	consumer_secret = getCredentials("twitterCredentials.json")['consumer_secret']
	access_token = getCredentials("twitterCredentials.json")['access_token']
	access_token_secret = getCredentials("twitterCredentials.json")['access_token_secret']

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	return tweepy.API(auth)

# Sends a tweet
def sendTweet(message):
	api = login_api()
	tweet = message
	status = api.update_status(status=tweet)

# Likes all tweets on the timeline	
def likeTweet():
	api = login_api()
	for tweet in tweepy.Cursor(api.search, q='#ocean').items():
		try:
			print('Tweet from: @' + tweet.user.screen_name)
			
			tweet.favorite()
			print('Retweeted the tweet')
		except tweepy.TweepError as e:
			print(e.reason)
			
		except StopIteration:
			break
	
if __name__ == "__main__":
	likeTweet()
			
