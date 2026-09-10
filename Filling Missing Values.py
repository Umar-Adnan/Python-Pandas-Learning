import pandas as pd
import numpy as np

# Sample dataset representing employee records
data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Age': [25, 34, None, 42, 29, 38, np.nan, 29],
    'Salary': [50000, 72000, 61000, 110000, 58000, np.nan, 92000, 61000],
    'Department': ['IT', 'HR', 'IT', 'Finance', np.nan, 'HR', 'Finance', 'IT'],
    'Remote_Worker': [True, np.nan, True, False, True, False, True, True]
}

df = pd.DataFrame(data)
df.insert(1, "Employee Name", ["Umar", "Nomi", "Fasih", None, "Khan", "Saif", "Tayyab", np.nan])
print("Original DataFrame Without Filling Missing Values:\n", df)
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print("After filling Age & Salary Column with mean values:\n", df)
print("============================================================")

print("============================================================")
df["Employee Name"] = df["Employee Name"].fillna("Missing")
print("After removing missing values from Employee name column:\n", df)