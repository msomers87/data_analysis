
from high_school_main import student_math, student_portuguese
from scipy.stats import ttest_ind

# Function to calculate and print statistics for a given column
def calculate_and_print_stats(data, column_name, subject):
    # Calculate and print average
    average = round(data[column_name].mean(), 1)
    print(f"Average {subject} {column_name}: {average}")

    # Calculate and print median
    median = data[column_name].median()
    print(f"Median {subject} {column_name}: {median}")

    # Calculate and print mode
    mode = data[column_name].mode().iloc[0]
    print(f"Mode {subject} {column_name}: {mode}")

# Columns for math grades
math_columns = ['grade_1', 'grade_2', 'final_grade']

# Columns for language grades
language_columns = ['grade_1', 'grade_2', 'final_grade']

# Calculate and print statistics for math grades
for column in math_columns:
    calculate_and_print_stats(student_math, column, "Math")

# Calculate and print statistics for language grades
for column in language_columns:
    calculate_and_print_stats(student_portuguese, column, "Portuguese")

# Calculate average final grades for 'Apart' and 'Living together' for Math
average_math_apart = student_math[student_math['parent_status'] == 'Apart']['final_grade'].mean()
average_math_together = student_math[student_math['parent_status'] == 'Living together']['final_grade'].mean()

# Calculate average final grades for 'Apart' and 'Living together' for Portuguese
average_portuguese_apart = student_portuguese[student_portuguese['parent_status'] == 'Apart']['final_grade'].mean()
average_portuguese_together = student_portuguese[student_portuguese['parent_status'] == 'Living together']['final_grade'].mean()

# Calculate t-test for Math
grades_math_apart = student_math[student_math['parent_status'] == 'Apart']['final_grade']
grades_math_together = student_math[student_math['parent_status'] == 'Living together']['final_grade']
t_stat_math, p_value_math = ttest_ind(grades_math_apart, grades_math_together)

# Calculate t-test for Portuguese
grades_portuguese_apart = student_portuguese[student_portuguese['parent_status'] == 'Apart']['final_grade']
grades_portuguese_together = student_portuguese[student_portuguese['parent_status'] == 'Living together']['final_grade']
t_stat_portuguese, p_value_portuguese = ttest_ind(grades_portuguese_apart, grades_portuguese_together)

# Print the results
print(f"Average final grade for 'Apart' (Math): {average_math_apart}")
print(f"Average final grade for 'Living together' (Math): {average_math_together}")
print(f"T-test results for Math:")
print(f"T-statistic: {t_stat_math}")
print(f"P-value: {p_value_math}")
print("Statistically significant" if p_value_math < 0.05 else "Not statistically significant")

print(f"Average final grade for 'Apart' (Portuguese): {average_portuguese_apart}")
print(f"Average final grade for 'Living together' (Portuguese): {average_portuguese_together}")
print("T-test results for Portuguese:")
print(f"T-statistic: {t_stat_portuguese}")
print(f"P-value: {p_value_portuguese}")
print("Statistically significant" if p_value_portuguese < 0.05 else "Not statistically significant")


