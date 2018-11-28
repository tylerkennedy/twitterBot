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
			
			
"""Structure for tic-tac-toe bot"""

class game:

	# Constructor for the game
	def __init__(self):
		
	def detect_tag():
		# Run this on loop to listen for when the bot is tagged in a new thread
		# Determine if this is a new thread or not

	def get_user_tag()
	def tweet_user(message):
		api = login_api()
		tweet = message
		status = api.update_status(status=tweet)

	board = {}
	def build_board():
		"""
		1 | 2 | 3
		- + - + -
		4 | 5 | 6
		- + - + -
		7 | 8 | 9
	
		"""
		global board
		board = {1 : "none", 2 : "none", 3 : "none", 4 : "none", 5 : "none", 6 : "none", 7 : "none", 8 : "none", 9 : "none"}
	
	def start_game():
	
	
		# This should be what the user says to the bot to communicate with it
		if(response.upper() == "START"):
			build_board()
			#
			tweet_user
	def main():
		# Call all functions necessary for the bot
if __name__ == "__main__":
	main()
			
