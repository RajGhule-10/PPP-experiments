print("SY-5", "Raj Ghule", "Roll_no-40")

import pandas as pd

data = {
    'StudyHours': [1, 2, 3, 4, 5],
    'SleepHours': [7, 6, 6, 5, 5],
    'Score': [35, 45, 50, 60, 70]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

X = df[['StudyHours', 'SleepHours']]

y = df['Score']

print("\nIndependent Variables (X):")
print(X)

print("\nDependent Variable (y):")
print(y)