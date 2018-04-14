import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

'''
This class has all the NLP methods for text preprocessing including:

Tokenzie.
Convert each token to be in lower case.
Parts of speech tagging: nouns, verbs, adjectives, and advers.
Stop word removel (standard): Remove words from the Default English stopwords list.
Stop word removel (custom): ['.','(',')','/','will','i',',','the', 'he','she']
Lemmatize: Reduce each word to its lemma.

'''

class NLP:

    def tokenize(all_tweets):
        new_list = []
        for tweet in all_tweets:
            new_list.append(word_tokenize(tweet[0]))
        return new_list

    def lower_case(tweet_as_token):
        new_list = []
        for tweet in tweet_as_token:
            lst = []
            for token in tweet:
                lst.append(token.lower())
            new_list.append(lst)
        return new_list


    def parts_of_speech(tweet_as_token):
        new_list = []
        part_of_speech = ['RB','JJ','NN','VBP']
        for tweet in tweet_as_token:
            lst = []
            for token in nltk.pos_tag(tweet):
                if token in part_of_speech:
                    print(tweet)
                    lst.append(token)
            new_list.append(lst)
        return new_list

    def parts_of_speech(data):
        newDict = {}
        part_of_speech = ['RB','JJ','NN','VBP']
        for tweet in data:
            for t in tweet:
                print(t)
                lst = []
                for word in nltk.pos_tag(t):
                    if word[1] in part_of_speech:
                        print(word[0])
                        lst.append(word[0])
                newDict.update({tweet: lst})
        return newDict

    def parts(all):
        ret_lst = []
        part_of_speech = ['RB', 'JJ', 'NN', 'VBP']
        for i in all:
            temp_lst = []
            for t in nltk.pos_tag(i):
                if t[1] in part_of_speech:
                    temp_lst.append(t[0])
            ret_lst.append(temp_lst)
        return ret_lst

    def stop_word_removal(tweet_as_token):
        new_list = []
        custom_list = ['.','(',')','/','will','i',',','the', 'he','she',]
        list_of_list = custom_list + stopwords.words("english")
        for tweet in tweet_as_token:
            lst = []
            for token in tweet:
                if token not in list_of_list:
                    lst.append(token)
            new_list.append(lst)
        return new_list


    def lemmatize(tweet_as_token):
        new_list = []
        lst = []
        lemmatizer = WordNetLemmatizer()
        for tweet in tweet_as_token:
            for token in tweet:
                lst.append(lemmatizer.lemmatize(token))
            new_list.append(lst)
            lst = []
        return new_list

