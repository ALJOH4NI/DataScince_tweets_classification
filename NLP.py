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

class NLP_text:

    def lower_case(data):
        dict = {}
        for key, value in data.items():
            lst = []
            [lst.append(i.lower()) for i in value]
            dict.update({key: lst})
        return dict


    def parts_of_speech(data):
        newDict = {}
        part_of_speech = ['RB','JJ','NN','VBP']
        for key,k in data.items():
            lst = []
            for word in nltk.pos_tag(k):
                if word[1] in part_of_speech:
                    lst.append(word[0])
            newDict.update({key: lst})
        return newDict


    def stop_word_removal(dict):
        newDict = {}
        custom_list = ['.','(',')','/','will','i',',','the', 'he','she']
        list_of_list = custom_list + stopwords.words("english")
        for key, value in dict.items():
            lst = []
            for word in value:
                if word not in list_of_list:
                    lst.append(word)
            newDict.update({key: lst})
        return newDict


    def tokenize(dict):
        new_dict = {}
        for key, value in dict.items():
            new_dict.update({key: word_tokenize(value)})
        return new_dict


    def lemmatize(data):
        dict = {}
        lst = []
        lemmatizer = WordNetLemmatizer()
        for key, value in data.items():
            for word in value:
                lst.append(lemmatizer.lemmatize(word))
            dict.update({key: lst})
            lst = []
        return dict
