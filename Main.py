from ReadCSV import CSV


class Main:
    tweets = []
    def getDataCSV(self):
        tweets = CSV.get_cvs(self)
        return tweets

    def print_tweets(self):
        temp = []; temp = self.getDataCSV()
        for tweet in temp:
            print(tweet)







'''
Call methods
'''
MainObj = Main()
MainObj.print_tweets()