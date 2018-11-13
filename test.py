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
def main():
	api = login_api()
	tweet = "My first tweet"
	status = api.update_status(status=tweet)
	
	
if __name__ == "__main__":
	main()
			
