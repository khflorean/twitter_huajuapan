from decouple import config
import twitter

# Initialize client
api_client = twitter.Api(
	consumer_key=config('CONSUMER_KEY'),
	consumer_secret=config('CONSUMER_SECRET'),
	access_token_key=config('ACCESS_TOKEN_KEY'),
	access_token_secret=config('ACCESS_TOKEN_SECRET')
)


# Checking credentials out
#print(api_client.VerifyCredentials())

#result=api_client.PostUpdate("Python test OLIN")
#print(result)

#image_path = os.path.abspath('image.jpg')

result = api_client.PostUpdate("@HerubielFlorean OLIN2")

print(result)