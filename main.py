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

    fetch_tweet = api.user_timeline(id=self_id, count=1, tweet_mode="extended")[0]
    last_tweet = fetch_tweet.full_text

    return last_tweet


def get_tweet():
    last_tweet = getLastTweet()
    file = open("tweets.txt", "r")

    content = file.read()
    tweet_list = content.split("\n")
    idx = 0
    print(type(last_tweet), last_tweet)

    for i, line in enumerate(tweet_list):
        if line == last_tweet:
            idx = i + 1
    if len(tweet_list[idx]) > 280:
        idx = idx + 1
    return tweet_list[idx]


def tweet():
    api = authenticate()
    msg = get_tweet()
    print(msg)
    api.update_status(msg)


def main():
    while True:
        tweet()
        time.sleep(18000)


if __name__ == "__main__":
    main()
