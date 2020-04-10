from Config import *
import TweetExtractor
import Sia30Flagger

tweetExtractor = TweetExtractor.TweetExtractor(APP_KEY, APP_SECRET)
def getAllUsrTweets():
    username = input("What username?")
    tweets = tweetExtractor.getAllTweets(username)
    print(len(tweets))
    print((tweets[0]).keys())
    return tweets


def filter(tweets):
    tweets_list = tweetExtractor.extractTweetsTextWithRef(tweets)
    sia30Flagger = Sia30Flagger.Sia30Flagger()
    return sia30Flagger.filterSia30(tweets_list)

sia30Flagger = Sia30Flagger.Sia30Flagger()
sia30Flagger.writeUniqueFilteredTweetsReport(sia30Flagger.groupByFilteredSia30(filter(getAllUsrTweets())))

print("Open output.html")
