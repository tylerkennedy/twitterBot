"""
import tweepy
import json
import random

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
	api = tweepy.API(auth, wait_on_rate_limit=True)
	tweet = message
	status = api.update_status(tweet, id)

			
"""
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
twitterStream.filter(track=["@t3_gamebot"])
"""
"""

class game_thread(object):
	def __init__(self, screen_name, last_tweetid):
		self.screen_name = screen_name
		self.last_tweetid = last_tweetid
		self.game_active = True
		self.turn_count = 0

		self.board = {}
		self.who_won = ''
		self.spots_available = 9
		self.spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]

		self.build_board()

	def set_last_tweetid(self, last_tweetid):
		self.last_tweetid = ltid

	def set_game_active(self, game_active):
		self.game_active = ga

	def increase_turn_count(self):
		self.turn_count = self.turn_count + 1

	def build_board(self):
			#	
			#	1 | 2 | 3
			#	- + - + -
			#	4 | 5 | 6
			#	- + - + -
			#	7 | 8 | 9
			#	
		
			self.board = {1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9"}
	
	def output_board(self):
		output = ""
		output = (str(self.board.get(1)) + " | " + str(self.board.get(2)) + " | " + str(self.board.get(3)) + "\n" 
		+ "- + - + -\n"
		+ str(self.board.get(4)) + " | " + str(self.board.get(5)) + " | " + str(self.board.get(6)) + "\n"
		+ "- + - + -\n" 
		+ str(self.board.get(7)) + " | " + str(self.board.get(8)) + " | " + str(self.board.get(9)) + "\n")
		return output

	def three_in_a_row(self):


		if(self.board.get(1) == "x" and self.board.get(2) == "x" and self.board.get(3) == "x"):
			self.who_won = 'x'
			return True
		if(self.board.get(4) == "x" and self.board.get(5) == "x" and self.board.get(6) == "x"):
			self.who_won = 'x'
			return True
		if(self.board.get(7) == "x" and self.board.get(8) == "x" and self.board.get(9) == "x"):
			self.who_won = 'x'
			return True
		if(self.board.get(1) == "x" and self.board.get(4) == "x" and self.board.get(7) == "x"):
			self.who_won = 'x'
			return True
		if(self.board.get(2) == "x" and self.board.get(5) == "x" and self.board.get(8) == "x"):
			self.who_won = 'x'
			return True
		if(self.board.get(3) == "x" and self.board.get(6) == "x" and self.board.get(9) == "x"):
			self.who_won = 'x'
			return True
		if(self.board.get(1) == "x" and self.board.get(5) == "x" and self.board.get(9) == "x"):
			self.who_won = 'x'
			return True
		if(self.board.get(3) == "x" and self.board.get(5) == "x" and self.board.get(7) == "x"):
			self.who_won = 'x'
			return True

		if(self.board.get(1) == "o" and self.board.get(2) == "o" and self.board.get(3) == "o"):
			self.who_won = 'o'
			return True
		if(self.board.get(4) == "o" and self.board.get(5) == "o" and self.board.get(6) == "o"):
			self.who_won = 'o'
			return True
		if(self.board.get(7) == "o" and self.board.get(8) == "o" and self.board.get(9) == "o"):
			self.who_won = 'o'
			return True
		if(self.board.get(1) == "o" and self.board.get(4) == "o" and self.board.get(7) == "o"):
			self.who_won = 'o'
			return True
		if(self.board.get(2) == "o" and self.board.get(5) == "o" and self.board.get(8) == "o"):
			self.who_won = 'o'
			return True
		if(self.board.get(3) == "o" and self.board.get(6) == "o" and self.board.get(9) == "o"):
			self.who_won = 'o'
			return True
		if(self.board.get(1) == "o" and self.board.get(5) == "o" and self.board.get(9) == "o"):
			self.who_won = 'o'
			return True
		if(self.board.get(3) == "o" and self.board.get(5) == "o" and self.board.get(7) == "o"):
			self.who_won = 'o'
			return True

	def make_move(self,spot):
		
	
		if(self.board.get(spot) != "x" or self.board.get(spot) != "o"):
			self.board[spot] = 'x'
			self.spots_available = self.spots_available - 1
			self.spots.remove(spot)
			if(self.three_in_a_row() == True):
				print("WHO WON: " + self.who_won)
				self.spots_available = 0
				return	
			print(self.output_board())

		if(self.spots_available > 0):
			if(self.board.get(spot) != "x" or self.board.get(spot) != "o"):
				current_spot = random.choice(self.spots)
				self.board[current_spot] = 'o'
				self.spots_available = self.spots_available - 1
				self.spots.remove(current_spot)
				if(self.three_in_a_row() == True):
					print("WHO WON: " + self.who_won)
					self.spots_available = 0
					return
				print(self.output_board())


# Gather all tweets where the bot is mentioned

def gather_mentions():
	mentions = []
	mentions = tweepy.API(auth).search(q="@t3_gamebot")
	
	return mentions



games = [] 
#games = [{screen_name: "@t3_gamebot", last_tweetid: "1095341780084477956", game_active: True}]

mentions = gather_mentions()
for mention in mentions:
	
	screen_name = mention.user.screen_name
	last_tweetid = mention.id
	
	games.append(game_thread(screen_name, last_tweetid))
	print(screen_name)
	print(last_tweetid)
	#sendTweet("@" + str(screen_name) + " Let's play a game of tic tac toe! \n\n" + game_thread.output_board(), mention.id)

for game in games:
	sendTweet("@" + str(game.screen_name) + " Let's play a game of tic tac toe! \n\n" + game.output_board(), game.last_tweetid)
	
while True:
	mentions = gather_mentions()
	
	for mention in mentions:
		screen_name = mention.user.screen_name
		last_tweetid = mention.id

		gamenames = []
		for game in games:
			gamenames.append(game.screen_name)
			
			if(screen_name not in gamenames):
				games.append(game_thread(screen_name, last_tweetid))
				sendTweet("@" + str(game.screen_name) + " Let's play a game of tic tac toe! \n\n" + game.output_board(), game.last_tweetid)
				
			else:
				game.increase_count()
				game.make_move(mention.text)
				game.three_in_a_row()
				game.set_last_tweetid(self, mention.id)
				sendTweet("@" + str(game.screen_name) + "\n" + game.output_board(), game.last_tweetid)

"""
	
"""
	if(game.last_tweetid not in games):
		
		games.append(mention.id)
		sendTweet("@" + str(screen_name) + " Let's play a game of tic tac toe! \n\n" + output_board(), mention.id)
		print("Tweet sent")

	else:
		sendTweet("@" + str(screen_name) + " Please finish your last game ", mention.id)
"""




"""
while(len(spots) > 0 and spots_available > 0):
	make_move(random.choice(spots))


print(output_board())

"""

import tweepy
import json
import random
import re

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
api =  tweepy.API(auth)


# Sends a tweet
def sendTweet(message, id):
	api = tweepy.API(auth, wait_on_rate_limit=True)
	tweet = message
	status = api.update_status(tweet, id)


class game(object):
	def __init__(self, screen_name, last_tweetid):
		self.screen_name = screen_name
		self.last_tweetid = last_tweetid
		self.game_active = True

		self.board = {}
		self.who_won = ''
		self.spots_available = 9
		self.spots = [1, 2, 3, 4, 5, 6, 7, 8, 9]

		self.build_board()

	def set_last_tweetid(self, ltid):
		self.last_tweetid = ltid

	def set_game_active(self, game_active):
		self.game_active = ga

	def build_board(self):
			#	
			#	1 | 2 | 3
			#	- + - + -
			#	4 | 5 | 6
			#	- + - + -
			#	7 | 8 | 9
			#	
		
			self.board = {1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9"}
	
	def output_board(self):
		output = ""
		output = (str(self.board.get(1)) + " | " + str(self.board.get(2)) + " | " + str(self.board.get(3)) + "\n" 
		+ "- + - + -\n"
		+ str(self.board.get(4)) + " | " + str(self.board.get(5)) + " | " + str(self.board.get(6)) + "\n"
		+ "- + - + -\n" 
		+ str(self.board.get(7)) + " | " + str(self.board.get(8)) + " | " + str(self.board.get(9)) + "\n")
		return output

	def three_in_a_row(self):


		if(self.board.get(1) == "x" and self.board.get(2) == "x" and self.board.get(3) == "x"):
			self.who_won = 'x'
			return True
		if(self.board.get(4) == "x" and self.board.get(5) == "x" and self.board.get(6) == "x"):
			self.who_won = 'x'
			return True
		if(self.board.get(7) == "x" and self.board.get(8) == "x" and self.board.get(9) == "x"):
			self.who_won = 'x'
			return True
		if(self.board.get(1) == "x" and self.board.get(4) == "x" and self.board.get(7) == "x"):
			self.who_won = 'x'
			return True
		if(self.board.get(2) == "x" and self.board.get(5) == "x" and self.board.get(8) == "x"):
			self.who_won = 'x'
			return True
		if(self.board.get(3) == "x" and self.board.get(6) == "x" and self.board.get(9) == "x"):
			self.who_won = 'x'
			return True
		if(self.board.get(1) == "x" and self.board.get(5) == "x" and self.board.get(9) == "x"):
			self.who_won = 'x'
			return True
		if(self.board.get(3) == "x" and self.board.get(5) == "x" and self.board.get(7) == "x"):
			self.who_won = 'x'
			return True

		if(self.board.get(1) == "o" and self.board.get(2) == "o" and self.board.get(3) == "o"):
			self.who_won = 'o'
			return True
		if(self.board.get(4) == "o" and self.board.get(5) == "o" and self.board.get(6) == "o"):
			self.who_won = 'o'
			return True
		if(self.board.get(7) == "o" and self.board.get(8) == "o" and self.board.get(9) == "o"):
			self.who_won = 'o'
			return True
		if(self.board.get(1) == "o" and self.board.get(4) == "o" and self.board.get(7) == "o"):
			self.who_won = 'o'
			return True
		if(self.board.get(2) == "o" and self.board.get(5) == "o" and self.board.get(8) == "o"):
			self.who_won = 'o'
			return True
		if(self.board.get(3) == "o" and self.board.get(6) == "o" and self.board.get(9) == "o"):
			self.who_won = 'o'
			return True
		if(self.board.get(1) == "o" and self.board.get(5) == "o" and self.board.get(9) == "o"):
			self.who_won = 'o'
			return True
		if(self.board.get(3) == "o" and self.board.get(5) == "o" and self.board.get(7) == "o"):
			self.who_won = 'o'
			return True

	def make_move(self,spot):
		
	
		if(self.board.get(spot) != "x" or self.board.get(spot) != "o"):
			spot = spot[10:]
			spot = int(re.search(r'\d+', spot).group())
			print(spot)
			self.board[spot] = 'x'
			self.spots_available = self.spots_available - 1
			self.spots.remove(spot)
			if(self.three_in_a_row() == True):
				#print("WHO WON: " + self.who_won)
				self.spots_available = 0
				self.who_won = 'You'
				sendTweet("@" + str(self.screen_name) + " \n" + self.who_won + " Won the game \n" + self.output_board(), self.last_tweetid)
				return	
			#print(self.output_board())

		else:
			return " This spot is already taken, choose another one"

		if(self.spots_available > 0):
			if(self.board.get(spot) != "x" or self.board.get(spot) != "o"):
				current_spot = random.choice(self.spots)
				self.board[current_spot] = 'o'
				self.spots_available = self.spots_available - 1
				self.spots.remove(current_spot)
				if(self.three_in_a_row() == True):
					#print("WHO WON: " + self.who_won)
					self.spots_available = 0
					self.who_won = 'I'
					sendTweet("@" + str(self.screen_name) + " \n" + self.who_won + " Won the game \n" + self.output_board(), self.last_tweetid)
					return
				#print(self.output_board())


object = game("screen_name", 0)
games = {"@screen_name": object}

#override tweepy.StreamListener to add logic to on_status
class MyStreamListener(tweepy.StreamListener):

	def on_status(self, status):
		if(status.user.screen_name not in games.keys()):
			games.update({status.user.screen_name : game(status.user.screen_name, status.id)})
			sendTweet("@" + str(games[status.user.screen_name].screen_name) + " Let's play a game of tic tac toe! \n\n" + games[status.user.screen_name].output_board(), games[status.user.screen_name].last_tweetid)
		else:
			games[status.user.screen_name].make_move(status.text)
			games[status.user.screen_name].set_last_tweetid(status.id)
			sendTweet("@" + str(games[status.user.screen_name].screen_name) + " \n" + games[status.user.screen_name].output_board(), games[status.user.screen_name].last_tweetid)

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=MyStreamListener())

myStream.filter(track=['@t3_gamebot'])


