import pandas as pd

student_math = pd.read_csv('C:/Users/SMR/data_analysis/high_school_performances/student_math_clean.csv')
student_portuguese = pd.read_csv('C:/Users/SMR/data_analysis/high_school_performances/student_portuguese_clean.csv')


grade_1_math = []
for i in student_math['grade_1']:
    grade_1_math.append(i)

grade_2_math = []
for i in student_math['grade_2']:
    grade_2_math.append(i)

final_grade_math = []
for i in student_math['final_grade']:
    final_grade_math.append(i)

grade_1_language = []
for i in student_portuguese['grade_1']:
    grade_1_language.append(i)

grade_2_language = []
for i in student_portuguese['grade_2']:
    grade_2_language.append(i)

final_grade_language = []
for i in student_portuguese['final_grade']:
    final_grade_language.append(i)

def average_grade(list):
    sum = 0
    for grade in list:
        sum += grade
    return (sum/len(list))

average_grade_1_math = average_grade(grade_1_math)
print(average_grade_1_math)
