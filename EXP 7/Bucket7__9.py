print("SY-5", "Raj Ghule", "Roll_no-40")

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

data = {
    'Age': [20, 25, np.nan, 30, 35],
    'Marks': [80, np.nan, 70, 90, 85]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

print("\nAfter Imputation (NaN replaced with mean):")
print(df_imputed)

scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df_imputed), columns=df.columns)

print("\nAfter Scaling (Standardized Data):")
print(df_scaled)