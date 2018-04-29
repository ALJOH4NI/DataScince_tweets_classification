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
from sklearn import metrics
from Main import Main
from NLP import NLP

class StringMarching:

    CSVObj = CSV()
    targets = []
    s = 0

    bug = ['bug', 'fix', 'problem', 'issue', 'defect', 'crash', 'solve', 'error','help', 'trouble', 'please','support']
    feature_requests = ['add', 'could', 'would', 'hope', 'improve'
                        , 'miss', 'need', 'prefer', 'request', 'should',
                        'suggest', 'want', 'wish','future','later', 'update']
    user_experiences = ['assist', 'when', 'situation', 'confuse']

    list_of_tweets, comments, retweets, likes, target = CSVObj.get_cvs()

    for tweet in list_of_tweets:
        # for tweet in lst:
            bug_counter = 0
            FR_counter = 0
            UX_counter = 0
            for word in tweet:
                if word in bug:
                    bug_counter+=1
                elif word in feature_requests:
                    FR_counter+=1
                elif word in user_experiences:
                    UX_counter+=1
            su = sum([bug_counter, FR_counter, UX_counter])
            if bug_counter > FR_counter and  bug_counter > UX_counter:
                targets.append(0)
            elif FR_counter > bug_counter  and FR_counter > UX_counter:
                targets.append(1)
            elif UX_counter > FR_counter and UX_counter > bug_counter:
                targets.append(2)
            elif su == 0:
                targets.append(-1)
                s += 1
            elif su/3 == bug_counter:
                targets.append(3)
            else:
                print(tweet)
                print(bug_counter,FR_counter,UX_counter)
                print("============================")
                targets.append(-1)


    # print(classification_report(d, targets))
    # print(len(d), len(targets), s)
    # print(metrics.precision_score(d, targets, average=None)[0])
    # metrics.recall_score(d, targets, average=None)[0]
    # metrics.f1_score(d, targets, average=None)[0]
    #
    # metrics.precision_score(d, targets, average=None)[1]
    # metrics.recall_score(d, targets, average=None)[1]
    # metrics.f1_score(d, targets, average=None)[1]
    #
    # metrics.precision_score(d, targets, average=None)[2]
    # metrics.recall_score(d, targets, average=None)[2]
    # metrics.f1_score(d, targets, average=None)[2]

    # print(targets)
'''

bug = 0
FR = 1
UX = 2

d is the

bug_keys = ['bug', 'horrible', 'clashes', 'crashes', 'bad', 'older', 'mistake', 'terrible', 'awful', ':', ":'", '!' , 'not compatible', 'sucks', '?!']
predicted_basic_targets = classify_string_matching(bugs_data, bug_keys)
precision = metrics.precision_score(bugs_target, predicted_target_test, pos_label=1)
recall = metrics.recall_score(bugs_target, predicted_target_test, pos_label=1)
f1_score = metrics.f1_score(bugs_target, predicted_target_test, pos_label=1)

print(precision, recall, f1_score)

def classify_string_matching(user_reviews, keys):
    targets = []
    for review in user_reviews:
        bug = 0
        for word in review.split():
            if word in keys:
                bug += 1
        if bug > 0:
            targets.append(1)
        else:
            targets.append(0)
    return targets

'''