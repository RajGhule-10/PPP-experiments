print("SY-5", "Raj Ghule", "Roll_no-40")

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer

data = {
    'Age': [25, np.nan, 40, 35, np.nan, 50]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

imputer = SimpleImputer(strategy='mean')
df['Age'] = imputer.fit_transform(df[['Age']])

print("\nUpdated Dataset after Imputation:")
print(df)