import csv

with open('insurance.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)


    



