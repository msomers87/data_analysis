
from high_school_main import student_math, student_portuguese
from scipy.stats import ttest_ind

# Function to calculate and print statistics for a given variable
def calculate_and_print_stats(dataframe, variable):
    grades = dataframe[variable]

    # Calculate and print average
    average = round(grades.mean(), 1)
    print(f"Average {variable}: {average}")

    # Calculate and print median
    median = round(grades.median(), 1)
    print(f"Median {variable}: {median}")

    # Calculate and print mode
    mode = grades.mode()
    if not mode.empty:
        mode_value = mode.iloc[0]
        print(f"Mode {variable}: {mode_value}")
    else:
        print(f"No mode found for {variable}")

# Example usage
calculate_and_print_stats(student_math, 'final_grade')


# Calculate averages for subgroups
def calculate_average_for_subgroups(dataframe, column_name, variable):
    values = dataframe[column_name].unique()
    for value in values:
        subset = dataframe[dataframe[column_name] == value]
        average = round(subset[variable].mean(), 1)
        print(f"Average {variable} for {column_name} = {value}: {average}")

# Example usage
calculate_average_for_subgroups(student_math, 'sex', 'final_grade')


# Calculate t-test for Math
grades_math_apart = student_math[student_math['parent_status'] == 'Apart']['final_grade']
grades_math_together = student_math[student_math['parent_status'] == 'Living together']['final_grade']
t_stat_math, p_value_math = ttest_ind(grades_math_apart, grades_math_together)

# Calculate t-test for Portuguese
grades_portuguese_apart = student_portuguese[student_portuguese['parent_status'] == 'Apart']['final_grade']
grades_portuguese_together = student_portuguese[student_portuguese['parent_status'] == 'Living together']['final_grade']
t_stat_portuguese, p_value_portuguese = ttest_ind(grades_portuguese_apart, grades_portuguese_together)

# Print the results
print(f"T-test results for Math:")
print(f"T-statistic: {t_stat_math}")
print(f"P-value: {p_value_math}")
print("Statistically significant" if p_value_math < 0.05 else "Not statistically significant")

print("T-test results for Portuguese:")
print(f"T-statistic: {t_stat_portuguese}")
print(f"P-value: {p_value_portuguese}")
print("Statistically significant" if p_value_portuguese < 0.05 else "Not statistically significant")


