import csv

class CSV:
    def get_cvs(self):
        tweets = []
        comments = []
        retweets = []
        likes = []
        target = []
        with open('tweets.csv') as csvfile:
            next(csvfile)
            read_cvs = csv.reader(csvfile)
            for row in read_cvs:
                tweets.append(row[1])
                comments.append(row[2])
                retweets.append(row[3])
                likes.append(row[4])
                target.append(row[5])
            return tweets, comments, retweets, likes, target

