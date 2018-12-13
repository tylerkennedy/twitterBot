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
def sendTweet(message, id):
	api = login_api()
	tweet = message
	status = api.update_status(status=tweet, in_reply_to_status= id)

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
			

# Gather all tweets where the bot is mentioned

metions = []


def gather_mentions():
	global mentions
	mentions = login_api().search(q="@b0t_b0y")
	
	print(mentions)
	return mentions
	
			
#gather_mentions()
games = {}
# {screen_name: "EX: @b0t_b0y", last_tweetid: "EX: 123456789", game_active:"EX: yes"}
for mention in gather_mentions():
	print(mention.id)
	sendTweet("@b0t_b0y this is a reply sent from the bot", mention.id)



"""Structure for tic-tac-toe bot"""

class game:

	# Constructor for the game
	def __init__(self):
		self.screen_name = ""
		self.last_tweetid = 0
		self.game_active = True
		self.get_screen_name()
		self.build_board()
		self.tweet_user("Thanks for starting a game of tic-tac-toe. Do you want to be X's or O's?")
		
		
		
		
"""		
		
	def detect_reply():
		# Run this on loop to listen for when the bot is tagged in a new thread
		# Determine if this is a new thread or not
		None

	def get_screen_name():
		# Get the tag of the user so we can continue the thread for the game
		self.screen_name = ""
		self.thread_id = 0
	def tweet_user(message):
		api = login_api()
		tweet = message
		status = api.update_status(status=tweet)
	
	

	board = {}
	
	def build_board():
		#	
		#	1 | 2 | 3
		#	- + - + -
		#	4 | 5 | 6
		#	- + - + -
		#	7 | 8 | 9
		#	
		
		global board
		board = {1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9"}
	
	def current_board():
		print(board)
		board_output = board[1] + " |  " + board[2] + "  | " + board[3] + "\n" + "- + - + - \n" + board[4] + " |  " + board[5] + "  | " + board[6] + "\n" + "- + - + - \n" + board[7] + " |  " + board[8] + "  | " + board[9] + "\n"
		
		return board_output
	build_board()
	print(current_board())
	tweet_user(current_board())
def main():
	# Call all functions necessary for the bot
	None
		

		
		
		
if __name__ == "__main__":
	main()
			
#"""	