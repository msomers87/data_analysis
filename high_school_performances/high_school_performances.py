import pandas as pd
import numpy as np

# Load datasets
student_math = pd.read_csv('C:/Users/SMR/data_analysis/high_school_performances/student_math_clean.csv')
student_portuguese = pd.read_csv('C:/Users/SMR/data_analysis/high_school_performances/student_portuguese_clean.csv')

# Function to calculate average grade using NumPy
def average_grade_numpy(grades):
    return round(np.mean(grades), 1)

# Extract grades from columns
grade_1_math = student_math['grade_1']
grade_2_math = student_math['grade_2']
final_grade_math = student_math['final_grade']

grade_1_language = student_portuguese['grade_1']
grade_2_language = student_portuguese['grade_2']
final_grade_language = student_portuguese['final_grade']

# Calculate and print average grades using NumPy
average_grade_1_math = average_grade_numpy(grade_1_math)
print("Average Grade 1 (Math):", average_grade_1_math)

average_grade_2_math = average_grade_numpy(grade_2_math)
print("Average Grade 2 (Math):", average_grade_2_math)

average_final_grade_math = average_grade_numpy(final_grade_math)
print("Average Final Grade (Math):", average_final_grade_math)

average_grade_1_language = average_grade_numpy(grade_1_language)
print("Average Grade 1 (Language):", average_grade_1_language)

average_grade_2_language = average_grade_numpy(grade_2_language)
print("Average Grade 2 (Language):", average_grade_2_language)

average_final_grade_language = average_grade_numpy(final_grade_language)
print("Average Final Grade (Language):", average_final_grade_language)

# Calculate and print median using Pandas
median_grade_1_math = grade_1_math.median()
print("Median Grade 1 (Math):", median_grade_1_math)

median_grade_2_math = grade_2_math.median()
print("Median Grade 2 (Math):", median_grade_2_math)

median_final_grade_math = final_grade_math.median()
print("Median Final Grade (Math):", median_final_grade_math)

median_grade_1_language = grade_1_language.median()
print("Median Grade 1 (Language):", median_grade_1_language)

median_grade_2_language = grade_2_language.median()
print("Median Grade 2 (Language):", median_grade_2_language)

median_final_grade_language = final_grade_language.median()
print("Median Final Grade (Language):", median_final_grade_language)


# Calculate and print mode using Pandas
mode_grade_1_math = grade_1_math.mode().iloc[0]
print("Mode Grade 1 (Math):", mode_grade_1_math)

mode_grade_2_math = grade_2_math.mode().iloc[0]
print("Mode Grade 2 (Math):", mode_grade_2_math)

mode_final_grade_math = final_grade_math.mode().iloc[0]
print("Mode Final Grade (Math):", mode_final_grade_math)

mode_grade_1_language = grade_1_language.mode().iloc[0]
print("Mode Grade 1 (Language):", mode_grade_1_language)

mode_grade_2_language = grade_2_language.mode().iloc[0]
print("Mode Grade 2 (Language):", mode_grade_2_language)

mode_final_grade_language = final_grade_language.mode().iloc[0]
print("Mode Final Grade (Language):", mode_final_grade_language)
