import csv

def read_csv(file_path):
    data = {'age': [], 'sex': [], 'bmi': [], 'children': [], 'smoker': [], 'region': [], 'charges': []}
    
    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            for key in data.keys():
                data[key].append(row[key])

    return data

def calculate_average(data_list):
    try:
        return round(sum(map(float, data_list)) / len(data_list), 2)
    except ZeroDivisionError:
        return 0.0  # Handle the case where the list is empty

def count_occurrences(data_list, value):
    return data_list.count(value)

if __name__ == "__main__":
    file_path = 'C:/Users/SMR/data_analysis/project_medical_insurance/insurance.csv'
    
    data = read_csv(file_path)

    average_age = calculate_average(data['age'])
    male_count = count_occurrences(data['sex'], 'male')
    female_count = count_occurrences(data['sex'], 'female')
    average_bmi = calculate_average(data['bmi'])
    average_children = calculate_average(data['children'])
    smoker_count = count_occurrences(data['smoker'], 'yes')
    nonsmoker_count = count_occurrences(data['smoker'], 'no')
    
    # Count occurrences of regions
    region_counts = {region: count_occurrences(data['region'], region) for region in set(data['region'])}

    average_charges = calculate_average(data['charges'])

    # Output the results
    print(f"Average Age: {average_age}")
    print(f"Male Count: {male_count}")
    print(f"Female Count: {female_count}")
    print(f"Average BMI: {average_bmi}")
    print(f"Average Children: {average_children}")
    print(f"Smoker Count: {smoker_count}")
    print(f"Non-Smoker Count: {nonsmoker_count}")
    print("Region Counts:")
    for region, count in region_counts.items():
        print(f"{region}: {count}")
    print(f"Average Charges: {average_charges}")


# Calculate difference in charges between smokers and non-smokers
def read_csv(file_path):
    data = {'smoker': [], 'charges': []}

    with open(file_path) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data['smoker'].append(row['smoker'])
            data['charges'].append(float(row['charges']))

    return data

def calculate_average_charges(data_list, category):
    # Calculate average charges for a specific category (e.g., smoker or non-smoker)
    category_charges = [charge for smoker, charge in zip(data_list['smoker'], data_list['charges']) if smoker == category]
    return round(sum(category_charges) / len(category_charges), 2) if category_charges else 0.0

if __name__ == "__main__":
    file_path = 'C:/Users/SMR/data_analysis/project_medical_insurance/insurance.csv'

    data = read_csv(file_path)

    average_charges_smoker = calculate_average_charges(data, 'yes')
    average_charges_nonsmoker = calculate_average_charges(data, 'no')

    # Output the results
    print(f"Average Charges for Smokers: {average_charges_smoker}")
    print(f"Average Charges for Non-Smokers: {average_charges_nonsmoker}")

    cost_difference = average_charges_smoker - average_charges_nonsmoker
    print(f"Cost Difference (Smokers - Non-Smokers): {cost_difference}")


            





    



