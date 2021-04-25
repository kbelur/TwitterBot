import tweepy
import time

consumer_key = ' '
consumer_secret = ' '

key = ''
secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
# api.update_status('Tweeter bot reporting for duty')

hashtag = ["remdesivir", "Icubeds", "icubed", "hospital", "covid19", "oxygen", "patient",
           "covid", "bangalore"]
tweetNumber = 20


tweets = tweepy.Cursor(api.search, hashtag).items(tweetNumber)


def searchTweet():
    for tweet in tweets:
        try:
            tweet.retweet()
            tweet.create_favorite()
            print("retweet done!")
            time.sleep(10)
        except tweepy.TweepError as e:
            print(e.reason)
            time.sleep(10)


if __name__ == "__main__":
    searchTweet()
