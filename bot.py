import tweepy # type: ignore
import random
import string

# Credentials
api_key = "t1R3o3tQbExScYcAItguMXkwZ"
api_secret = "8uf9izR8QkDOeYuTE66ENXtx93n6Co67FJ3hv1OhfdojtSiSMK"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAGkTuAEAAAAAP3gWUtZSyXOUrNF9YdSoueeOtx8%3DILOKUqZG80pNgUzKVItMWuKfc6cFDylFpMlqwo1F6VWP5QrTxX"
access_token = "1795451965935177728-ABYmUDtYWp1nlKBBqCUUcvw0z2GpmI"
access_token_secret = "ZOHk8X7rzoj02G3AnUVcFsrVqkpMbIQsadwFMs9YvTgYJ"

client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(bearer_token, api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)


def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string


i = 1
while i<100:
    length = 12  
    random_string = generate_random_string(length)
    client.create_tweet(text=random_string)