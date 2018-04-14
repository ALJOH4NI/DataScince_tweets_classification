import csv

class CSV:
    def get_cvs(self):
        with open('tweets.csv') as csvfile:
            read_cvs = csv.reader(csvfile)
            dataSet = list(read_cvs)
            return dataSet
