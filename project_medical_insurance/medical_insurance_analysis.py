import csv

with open('C:/Users/SMR/data_analysis/project_medical_insurance/insurance.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)


    



