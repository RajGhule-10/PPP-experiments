print("SY-5", "Raj Ghule", "Roll_no-40")

import pandas as pd

data = {
    'Attendance': [75, 80, 85, 90, 95],
    'Marks': [60, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


X = df[['Attendance']]

y = df['Marks']

print("\nFeature (X):")
print(X)

print("\nTarget (y):")
print(y)