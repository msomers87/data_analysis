import pandas as pd

# Load datasets
student_math = pd.read_csv('C:/Users/SMR/data_analysis/high_school_performances/student_math_clean.csv')
student_portuguese = pd.read_csv('C:/Users/SMR/data_analysis/high_school_performances/student_portuguese_clean.csv')

# Checking general information 
print(student_math.columns)
print(student_math['address_type'].unique())


