import csv

#convert csvfile into separate lists
with open('C:/Users/SMR/data_analysis/project_medical_insurance/insurance.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    age = []
    sex = []
    bmi = []
    children = []
    smoker = []
    region = []
    charges = []
    for row in reader:
        age.append(row['age'])
        sex.append(row['sex'])
        bmi.append(row['bmi'])
        children.append(row['children'])
        smoker.append(row['smoker'])
        region.append(row['region'])
        charges.append(row['charges'])

#calculate average age
sum_of_ages = 0
for record in age:
    sum_of_ages += int(record)
average_age = round(sum_of_ages / len(age), 1)

print("The average age in this dataset is " + str(average_age) + '.')

#calculate count male and female
male_count = 0
female_count = 0
for record in sex:
    if record == 'male':
        male_count += 1
    elif record == 'female':
        female_count += 1

print("The count of males in the dataset is: " + str(male_count) + '.')
print("The count of females in the dataset is: " + str(female_count) + '.')

#calculate average bmi
sum_of_bmis = 0
for record in bmi:
    sum_of_bmis += float(record)
average_bmi = round(sum_of_bmis / len(bmi), 1)

print("The average bmi in this dataset is " + str(average_bmi) + '.')

#calculate average count of children
sum_of_children = 0
for record in children:
    sum_of_children += int(record)
average_children = round(sum_of_children / len(children), 1)

print(average_children)










    



