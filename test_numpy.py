import numpy as np
# arr1 = np.array([85, 92, 78, 95, 88, 76, 91, 89])

# print(arr1)
# print(f"mean: {np.mean(arr1):.2f}")
# print(f"median: {np.median(arr1)}")
# print(f"standard deviation: {np.std(arr1)}")
# print(f"max: {np.max(arr1)}")
# print(f"variance: {np.var(arr1)}")

# random_arr = np.random.rand(3,3)
# print(random_arr)

# random_int = np.random.randint(0,100)
# print(random_int)

# arr1 = np.array([85, 92, 78, 95, 88, 76, 91, 89])
# passed = arr1>=80
# passing_scores = arr1[passed]
# print(passed)
# print(passing_scores)
# passing_scores2 = arr1[arr1>85]
# print(passing_scores2)
# print(arr1[(arr1>85) & (arr1<95)])

# Student grades for 5 students across 4 subjects
# Rows: Students, Columns: Math, Physics, Chemistry, Biology
# grades = np.array([
#     [85, 90, 78, 92],  # Student 1
#     [78, 85, 88, 79],  # Student 2
#     [92, 88, 95, 91],  # Student 3
#     [67, 72, 70, 68],  # Student 4
#     [88, 86, 90, 87]   # Student 5
# ])

# print("Student Grades (Math, Physics, Chemistry, Biology):")
# print(grades)
# print()

# # Calculate average grade per student
# student_avg = np.mean(grades, axis=1)  # axis=1 means row-wise
# print("Average grade per student:")
# for i, avg in enumerate(student_avg):
#     print(f"  Student {i+1}: {avg:.2f}")
# print()

# # Calculate average grade per subject
# subject_avg = np.mean(grades, axis=0)  # axis=0 means column-wise
# subjects = ['Math', 'Physics', 'Chemistry', 'Biology']
# print("Average grade per subject:")
# for subject, avg in zip(subjects, subject_avg):
#     print(f"  {subject}: {avg:.2f}")
# print()

# # Find best student
# best_student = np.argmax(student_avg) + 1
# print(f"Best student: Student {best_student} (avg: {np.max(student_avg):.2f})")

# # Find hardest subject
# hardest_subject_idx = np.argmin(subject_avg)
# print(f"Hardest subject: {subjects[hardest_subject_idx]} (avg: {np.min(subject_avg):.2f})")
import pandas as pd
# scores = pd.Series([85, 92, 78, 95, 88])
# print(scores)

# scores_named = pd.Series([85, 92, 78, 95, 88],index=['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'])
# print(scores_named)

data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'Age' : [23, 25, 22, 24, 23],
        'Math': [85, 78, 92, 67, 88],
        'Physics': [90, 85, 88, 72, 86]
       }
print(data)
df = pd.DataFrame(data)
print(df)
print(df.columns.tolist())
print(df.describe())
print(df.iloc[0])
print(df[df['Math']>85])

