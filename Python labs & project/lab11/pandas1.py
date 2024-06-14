import pandas as pd

# Define the students and their exam scores
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# Create a Pandas Series with students as index and exam scores as values
scores_series = pd.Series(exam_scores, index=students)
print(scores_series)
