import sys
import csv


def printCard(card):
    print(card)


with open(sys.argv[1], newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    firstrow = True
    labels = 'foo'
    for row in csvreader:
        if firstrow:
            labels = list(map(str.strip, row))
            firstrow = False
        else:
            values = list(map(str.strip, row))
            card = dict(zip(labels, values))
            printCard(card)
