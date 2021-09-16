import time

import tweepy

from os import environ
CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


def tweet():
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

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)

    api.update_status(msg)

def main():
    while True:
        tweet()
        time.sleep(43200)
if __name__ == "__main__":
    main()