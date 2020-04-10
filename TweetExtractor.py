class TweetExtractor():

    def __init__(self, APP_KEY, APP_SECRET):
        from twython import Twython
        self.twitter = Twython(APP_KEY, APP_SECRET)

    def getName(self):
        self.username = input("Enter screen_name?")

    def getTimeline(self, screen_name, count, max_id=None):
        if(max_id == None):
            return self.twitter.get_user_timeline(
                screen_name=screen_name, count=count)
        else:
            return self.twitter.get_user_timeline(
                screen_name=screen_name, count=count, max_id=max_id)

    def getLastID(self, user_timeline):
        return user_timeline[0]['id']-1

    def getAllTweets(self, screen_name):
        self.user_timeline = self.getTimeline(screen_name, 1)
        for _i in range(16):
            new200tweets = self.getTimeline(
                screen_name, 200, self.getLastID(self.user_timeline))
            self.user_timeline.extend(new200tweets)
        return self.user_timeline

    def extractTweetsText(self, user_timeline):
        return [item["text"] for item in user_timeline]

    def extractTweetsTextWithRef(self, user_timeline):
        return [{"text": item["text"], "id_str": item["id_str"]} for item in user_timeline]

    def writeToFile(self, user_timeline):
        import codecs
        file = codecs.open("output.txt", "w", "utf-8")
        file.write(user_timeline)
        file.close()