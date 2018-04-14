from ReadCSV import CSV
from NLP import NLP

'''
[['TwitchSupport', 'error code 0x3022001', '9', '4', '4']]

'''

class Main:
    tweets = []
    def getDataCSV(self):
        tweets = CSV.get_cvs(self)
        return tweets

    def get_only_tweets(self):
        lst = []; lst = self.getDataCSV()
        all_tweets = [];
        for tweet in lst:
            tweet_as_list = []
            tweet_as_list.append(tweet[1])
            all_tweets.append(tweet_as_list)
        return all_tweets

    def prprocessing_tweets(self):
        all_tweets = self.get_only_tweets()
        tweet_as_token = NLP.tokenize(all_tweets)
        print('tweet_as_token = ', tweet_as_token)
        tweet_in_lower_case = NLP.lower_case(tweet_as_token)
        print('tweet_in_lower_case = ', tweet_in_lower_case)
        tweet_stop_word_removal = NLP.stop_word_removal(tweet_in_lower_case)
        print('tweet_stop_word_removal = ',tweet_stop_word_removal)
        tweet_parts_of_speech = NLP.parts(tweet_stop_word_removal)
        print('tweet_parts_of_speech = ', tweet_parts_of_speech)
        tweet_lemmatize = NLP.lemmatize(tweet_parts_of_speech)
        print('tweet_lemmatize = ', tweet_lemmatize)










'''
Call methods
'''
MainObj = Main()
MainObj.prprocessing_tweets()