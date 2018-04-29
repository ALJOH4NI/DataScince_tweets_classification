from ReadCSV import CSV
from NLP import NLP
from scipy.sparse import hstack
from sklearn import tree
from sklearn import model_selection
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import numpy as np
from ReadCSV import CSV


class Main:

    def preprocessing_tweets(self, all_tweets):
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
        return all_tweets


    def listOflist(self,tweet):
        lst = []
        lst2 = []
        for n in tweet:
            lst.append(n)
            lst2.append(lst)
            lst = []
        return lst2



'''
Call main methods
'''
MainObj = Main()
CSVobj = CSV()
tweets,likes,retweets,comments,target = CSVobj.get_cvs()

# for i in tweets:
#     print(i)

'''
List of lists
'''
prepare_in_lstOflst = MainObj.listOflist(tweets)
'''
NLP
'''
tweets_NLP = MainObj.preprocessing_tweets(prepare_in_lstOflst)
final_lst = [] ; [final_lst.append(i[0]) for i in tweets_NLP]
# [print(i) for i in final_lst]

'''
Tf idf Vectorizer
'''
vectorizer = TfidfVectorizer()
data = vectorizer.fit_transform(final_lst)
tfidf_data = TfidfTransformer(norm="l2").fit_transform(data)
print(tfidf_data.shape)

'''
create 3 list one fro likes one foe commenrts and retweets
'''
likes_column = np.array(likes).reshape(len(tweets), 1)
retweets_column = np.array(retweets).reshape(len(tweets), 1)
comments_column = np.array(comments).reshape(len(tweets), 1)



'''
TODO: cant fit the metadata in the matrix

tfidf_data = hstack((tfidf_data, likes_column, retweets_column, comments_column))
print(tfidf_data.shape)

'''


'''
Applying differant classifiers
'''
test_multinominalNB_classifier = MultinomialNB()
tree = tree.DecisionTreeClassifier()
maxEnt = LogisticRegression()
test_multinominalNB_predcited = model_selection.cross_val_predict(maxEnt, tfidf_data, target, cv=10)
print(classification_report(target, test_multinominalNB_predcited))
print("The accuracy score for MultinomialNB using 10-Fold Cross Validation is {:.2%}".format(accuracy_score(target, test_multinominalNB_predcited)))
X_train, X_test, Y_train, Y_test = train_test_split(tfidf_data, target, test_size=0.30)
test_multinominalNB_classifier.fit(X_train, Y_train)
Y_pred = test_multinominalNB_classifier.predict(X_test)
print(classification_report(Y_test, Y_pred))