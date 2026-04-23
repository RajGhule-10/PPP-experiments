print("SY-5", "Raj Ghule", "Roll_no-40")

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

data = {
    'Age': [20, 21, np.nan, 23, 24, np.nan],
    'Marks': [80, np.nan, 75, 90, np.nan, 85]
}

df = pd.DataFrame(data)

print("Dataset BEFORE Imputation:")
print(df)

imputer = SimpleImputer(strategy='mean')

df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

print("\nDataset AFTER Imputation:")
print(df_imputed)