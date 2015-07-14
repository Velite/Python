import csv

with open('budget.csv', 'r') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',')
	for row in spamreader:
		print (', '.join(row))