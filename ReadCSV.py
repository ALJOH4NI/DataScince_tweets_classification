import csv


def get_cvs():
    with open('smarthome-userstories-1k.csv') as csvfile:
        read_cvs = csv.reader(csvfile)
        dataSet = list(read_cvs)
        return dataSet
