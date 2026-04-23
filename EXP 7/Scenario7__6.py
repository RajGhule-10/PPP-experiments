print("SY-5", "Raj Ghule", "Roll_no-40")

import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    'Runs': [100, 250, 300, 150, 400],
    'StrikeRate': [120, 130, 110, 140, 150]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

print("\nNormalized Dataset (after StandardScaler):")
print(df_scaled)