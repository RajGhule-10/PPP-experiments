print("SY-5", "Raj Ghule", "Roll_no-40")

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler

data = {
    'Age': [20, np.nan, 25, 30, np.nan],
    'Marks': [80, 85, np.nan, 90, 95]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)


imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

print("\nAfter Imputation:")
print(df_imputed)

scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df_imputed), columns=df.columns)

print("\nAfter Scaling:")
print(df_scaled)