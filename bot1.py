import tweepy
import time

consumer_key = ' '
consumer_secret = ' '

key = ''
secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(key, secret)

api = tweepy.API(auth)
api.update_status('Tweeter bot reporting for duty')

FILE_NAME = 'last_seen.txt'


def read_last_seen(FILE_NAME):
    file_read = open(FILE_NAME, 'r')
    last_seen_id = int(file_read.read().strip())
    file_read.close()
    return last_seen_id


def write_last_seen(FILE_NAME, last_seen_id):
    file_write = open(FILE_NAME, 'w')
    file_write.write(str(last_seen_id))
    file_write.close()
    return


tweets = api.mentions_timeline(read_last_seen(FILE_NAME), tweet_mode="extended")


def reply():
    for tweet in reversed(tweets):
        print(str(tweet.id) + " - " + tweet.full_text)
        if '#covid' in tweet.full_text.lower():
            print(str(tweet.id) + " - " + tweet.full_text)
            api.update_status('@' + tweet.user.screen_name + "Amplifying he tweet retweet and link", tweet.id)
            api.create_favorite(tweet.id)
            api.retweet(tweet.id)
            write_last_seen(tweet.id)


while True:
    reply()
    time.sleep(10)

# def main():
#     print("Starting my task")
#     while True:
#         check_hastag(api, ["urgent", "remdesivir", "bed", "icu", "hospital", "covid-19", "o2", "patient", "covid",
#                            "bangalore", "covid"])
#         time.sleep(60)
#
#
# if __name__ == "__main__":
#     main()
