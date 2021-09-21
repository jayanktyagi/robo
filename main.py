import time

import tweepy

from os import environ

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']


def authenticate():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)

    return api


def getLastTweet():
    api = authenticate()

    self_id = api.me().id

    fetch_tweet = api.user_timeline(id=self_id, count=1)[0]
    last_tweet = fetch_tweet.text

    return last_tweet


def tweet():
    api = authenticate()
    last_tweet = getLastTweet()
    file = open("tweets.txt", "r")

    content = file.read()
    tweet_list = content.split("\n")
    idx = 0

    for i, line in enumerate(tweet_list):
        if line != last_tweet:
            continue
        elif line == last_tweet:
            idx = i + 1

    msg = tweet_list[idx]
    print(msg)
    api.update_status(msg)


def main():
    while True:
        tweet()
        time.sleep(18000)


if __name__ == "__main__":
    main()
