
from high_school_main import student_math, student_portuguese
from scipy.stats import ttest_ind

# Input for functions
dataframe_input = student_math
variable_input = 'final_grade'
subgroup_input = 'address_type'

# Function to calculate and print statistics for a given variable
def calculate_and_print_stats(dataframe, variable):
    grades = dataframe[variable]

    # Calculate and print average
    average = round(grades.mean(), 1)
    print(f"Average {variable}: {average} (all students)")

    # Calculate and print median
    median = round(grades.median(), 1)
    print(f"Median {variable}: {median} (all students)")

    # Calculate and print mode
    mode = grades.mode()
    if not mode.empty:
        mode_value = mode.iloc[0]
        print(f"Mode {variable}: {mode_value} (all students)")
    else:
        print(f"No mode found for {variable} (all students)")

# Print central tendencies of total dataset
print("Central tendencies (total dataset):") 
calculate_and_print_stats(dataframe_input, variable_input)

# Calculate averages for subgroups
def calculate_average_for_subgroups(dataframe, column_name, variable):
    values = dataframe[column_name].unique()
    for value in values:
        subset = dataframe[dataframe[column_name] == value]
        average = round(subset[variable].mean(), 1)
        print(f"Average {variable} for {column_name} = {value}: {average}")

# Print central tendencies of subgroups
print('Central tendencies (subgroups):')
calculate_average_for_subgroups(dataframe_input, subgroup_input, variable_input)

# Function for t-test
def perform_t_test(dataframe, column_name, variable):
    values = dataframe[column_name].unique()
    subgroups = {value: dataframe[dataframe[column_name] == value][variable] for value in values}
    
    # Perform t-test between subgroups
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            subgroup1 = values[i]
            subgroup2 = values[j]
            
            t_stat, p_value = ttest_ind(subgroups[subgroup1], subgroups[subgroup2])
            
            print(f"T-test between {subgroup1} and {subgroup2}:")
            print(f"T-statistic: {t_stat}, p-value: {p_value}")
            
            if p_value < 0.05:  # Assuming significance level of 0.05
                print("The difference is statistically significant.")
            else:
                print("The difference is not statistically significant.")

# Perform t-test for subgroups
perform_t_test(dataframe_input, subgroup_input, variable_input)