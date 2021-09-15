import tweepy

from credentials import consumer_key, consumer_key_secret, access_token, access_token_secret

file = open("tweets.txt", "r")

content = file.read()
twitlist = content.split("\n")

with open("tweets.txt", "w") as fp:
    for i, line in enumerate(twitlist):
        if i == 0:
            msg = line
            print(line)
        if i != 0:
            fp.write(line+"\n")

file.close()

auth = tweepy.OAuthHandler(consumer_key, consumer_key_secret)

auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth);

api.update_status(msg)


