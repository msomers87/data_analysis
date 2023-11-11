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

#calculate count male and female
male_count = 0
female_count = 0
for record in sex:
    if record == 'male':
        male_count += 1
    elif record == 'female':
        female_count += 1

#calculate average bmi
sum_of_bmis = 0
for record in bmi:
    sum_of_bmis += float(record)
average_bmi = round(sum_of_bmis / len(bmi), 1)

#calculate average count of children
sum_of_children = 0
for record in children:
    sum_of_children += int(0)
average_children = round(sum_of_children / len(children), 1)

#calculate count smokers and nonsmokers.
smoker_count = 0
nonsmoker_count = 0
for record in smoker:
    if record == 'yes':
        smoker_count += 1
    elif record == 'no':
        nonsmoker_count += 1

#calculate count of regions
southeast_count = 0
southwest_count = 0
northeast_count = 0
northwest_count = 0
for record in region:
    if record == 'southeast':
        southeast_count += 1
    elif record == 'southwest':
        southwest_count += 1
    elif record == 'northeast':
        northeast_count += 1
    elif record == 'northwest':
        northwest_count += 1

#calculate average charges
sum_of_charges = 0
for record in charges:
    sum_of_charges += float(record)
average_charges = round(sum_of_charges / len(charges), 2)

#print statements averages and counts:
print("Average age: " + str(average_age))
print("Average bmi: " + str(average_bmi))
print("Average number of children: " + str(average_children))
print("Average charges: " + str(average_charges))
print("Number of males: " + str(male_count))
print("Number of females: " + str(female_count))
print("Number of smokers: " + str(smoker_count))
print("Number of non-smokers: " + str(nonsmoker_count))
print("Number of residents of region southeast: " + str(southeast_count))
print("Number of residents of region southwest: " + str(southwest_count))
print("Number of residents of region northeast: " + str(northeast_count))
print("Number of residents of region northwest: " + str(northwest_count))

#zip every list into 1 list
medical_insurance_list = list(zip(age,sex,bmi,children,smoker,region,charges))







    



