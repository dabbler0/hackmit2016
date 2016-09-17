import csv

with open('deleted_tweets.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    politicians = set()
    i = 0
    for row in reader:
        politicians.add(row[2])
        i += 1
        if i % 1000 == 0:
            print("%d" % (i))

print(politicians)
