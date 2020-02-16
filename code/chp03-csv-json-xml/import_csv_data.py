import csv

csv_file = open('../../data/chp3/data-text.csv', 'rb')
reader = csv.reader(csv_file)

for row in reader:
    print row
