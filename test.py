import tweepy
import json

# Read the credentials needed to authenticate with the api from a JSON file so the credentials are not published on GitHub
def getCredentials(fileLocation):
	with open(fileLocation, "r") as read_file:
		credentials = json.load(read_file)
		read_file.close()
	return credentials
	

consumer_key = getCredentials("twitterCredentials.json")['consumer_key']
consumer_secret = getCredentials("twitterCredentials.json")['consumer_secret']
access_token = getCredentials("twitterCredentials.json")['access_token']
access_token_secret = getCredentials("twitterCredentials.json")['access_token_secret']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#return tweepy.API(auth)

# Sends a tweet
def sendTweet(message, id):
	api = tweepy.API(auth)
	tweet = message
	status = api.update_status(tweet, id)

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
			
"""
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener


#consumer key, consumer secret, access token, access secret.
ckey = getCredentials("twitterCredentials.json")['consumer_key']
csecret = getCredentials("twitterCredentials.json")['consumer_secret']
atoken = getCredentials("twitterCredentials.json")['access_token']
asecret = getCredentials("twitterCredentials.json")['access_token_secret']

class listener(StreamListener):
    

    def on_data(self, data):
        print(data)
        return(True)

    def on_status(self, status):
        print("PLEASE WORK")
        print(status.text)
        sendTweet("@" + (status.entities['user_mentions'][0]['screen_name']) + "Lets play tic-tac-toe!", status.id)


    

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["@b0t_b0y"])
"""

# Gather all tweets where the bot is mentioned

metions = []


def gather_mentions():
	global mentions
	mentions = tweepy.API(auth).search(q="@t3_gamebot")
	
	print(mentions)
	return mentions


#gather_mentions()
games = []
# {screen_name: "EX: @b0t_b0y", last_tweetid: "EX: 123456789", game_active:"EX: yes"}
for mention in gather_mentions():
	screen_name = mention.user.screen_name
	print(screen_name)
	print(mention.id)
	sendTweet("@" + str(screen_name) + " Let's play a game of tic tac toe!", mention.id)
	"""
	if(mention.id not in games):
		games.append(mention.id)
		sendTweet("@" + str(screen_name) + " Let's play tic-tac-toe!", mention.id)
		print("Tweet sent")
	else:
		#sendTweet("@" + str(screen_name) + " starting a new game with your first reply", mention.id)
		print("No Tweet sent ")
	#sendTweet("@b0t_b0y this is a reply sent from the bot", mention.id)
	"""


#Structure for tic-tac-toe bot
"""
class game:

	# Constructor for the game
	def __init__(self):
		self.screen_name = ""
		self.last_tweetid = 0
		self.game_active = True
		self.get_screen_name()
		self.build_board()
		self.tweet_user("Thanks for starting a game of tic-tac-toe. Do you want to be X's or O's?")
		
		
		
		
		
		
	def detect_reply():
		# Run this on loop to listen for when the bot is tagged in a new thread
		# Determine if this is a new thread or not
		None

	def get_screen_name():
		# Get the tag of the user so we can continue the thread for the game
		self.screen_name = ""
		self.thread_id = 0
	def tweet_user(screen_name, message, id):
		api = login_api()
		tweet = screen_name + message
		status = api.update_status(tweet, id)
	
	

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