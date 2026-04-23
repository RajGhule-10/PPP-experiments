print("SY-5", "Raj Ghule", "Roll_no-40")

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import mean_squared_error, accuracy_score, confusion_matrix

data = {
    'Age': [25, 30, np.nan, 40, 50, np.nan, 60],
    'Treatments': [1, 2, 3, np.nan, 2, 1, 3],
    'LifestyleScore': [7, 6, 8, 5, np.nan, 6, 7],
    'MedicalCost': [2000, 3000, 4000, 5000, 6000, 7000, 8000],
    'Readmission': [0, 0, 1, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:\n", df)

imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

print("\nAfter Imputation:\n", df_imputed)

scaler = StandardScaler()

X = df_imputed[['Age', 'Treatments', 'LifestyleScore']]
X_scaled = scaler.fit_transform(X)


y_reg = df_imputed['MedicalCost']
y_clf = df_imputed['Readmission']

X_train, X_test, y_reg_train, y_reg_test, y_clf_train, y_clf_test = train_test_split(
    X_scaled, y_reg, y_clf, test_size=0.3, random_state=42, stratify=y_clf
)

lin_model = LinearRegression()
lin_model.fit(X_train, y_reg_train)
y_reg_pred = lin_model.predict(X_test)

mse = mean_squared_error(y_reg_test, y_reg_pred)

log_model = LogisticRegression()
log_model.fit(X_train, y_clf_train)
y_clf_pred = log_model.predict(X_test)

accuracy = accuracy_score(y_clf_test, y_clf_pred)
cm = confusion_matrix(y_clf_test, y_clf_pred)


print("\n--- Linear Regression (Medical Cost) ---")
print("Actual:", list(y_reg_test))
print("Predicted:", y_reg_pred)
print("MSE:", mse)

print("\n--- Logistic Regression (Readmission) ---")
print("Actual:", list(y_clf_test))
print("Predicted:", list(y_clf_pred))
print("Accuracy:", accuracy)
print("Confusion Matrix:\n", cm)