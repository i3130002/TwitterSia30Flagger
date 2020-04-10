import codecs


class Sia30Flagger():

    def __init__(self):
        self.sensitiveWords = ["جمهوری", "ج.ا", "اسلامی", "ایران", "مرگ", "جاعش", "خامنه", "احمدی نژاد",
                               "روحانی", "@azarijahromi", "اینا", "مجلس", "قوه قضاییه", "رئیس", "آخوند", "شاه ", "حجاب", "آمریکا"]

    def filterSia30(self, tweets_list):
        sensitiveTweets = []

        for i in range(len(tweets_list)):
            foundWords = []
            for j in range(len(self.sensitiveWords)):
                if(len(self.sensitiveWords[j]) == 0):
                    continue
                if tweets_list[i]["text"].find(self.sensitiveWords[j]) > -1:
                    foundWords.append(self.sensitiveWords[j])
            if len(foundWords) > 0:
                sensitiveTweets.append(
                    {"tweet": tweets_list[i], "foundWords": foundWords})
        return sensitiveTweets

    def groupByFilteredSia30(self, sensitiveTweets):
        uniqueId = {}
        for i in range(len(sensitiveTweets)):
            id_str = sensitiveTweets[i]["tweet"]["id_str"]
            if id_str in uniqueId.keys():
                uniqueId[id_str][0]["foundWords"] +=  ' '.join(
                    [str(elem)+" " for elem in sensitiveTweets[i]["foundWords"]])
            else:
                uniqueId[id_str] = []
                uniqueId[id_str].append({"foundWords": ' '.join(
                    [str(elem) for elem in sensitiveTweets[i]["foundWords"]])})
                uniqueId[id_str].append(
                    {"tweet": sensitiveTweets[i]["tweet"]})
        return uniqueId

    def writeUniqueFilteredTweetsReport(self, sensitiveTweets_unique):
        file = codecs.open("output.html", "w", "utf-8")
        file.write("<div style='direction: rtl;'>")
        for tweetKey in sensitiveTweets_unique.keys():
            file.write("<p><a target='_blank' href='https://twitter.com/i/web/status/" +
                       tweetKey + "'>"+sensitiveTweets_unique[tweetKey][1]["tweet"]["text"]+" < /a >")
            file.write(
                "       " + sensitiveTweets_unique[tweetKey][0]["foundWords"]+"</p>")
            file.write("<br>")

        file.write("</div>")
        file.close()
