import pandas as pd
import numpy as np

# 1. Dataset setup
data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Age': [25, 34, None, 42, 29, 38, np.nan, 29],
    'Salary': [50000, 72000, 61000, 110000, 58000, np.nan, 92000, 61000],
    'Department': ['IT', 'HR', 'IT', 'Finance', np.nan, 'HR', 'Finance', 'IT'],
    'Remote_Worker': [True, np.nan, True, False, True, False, True, True]
}

df = pd.DataFrame(data)
print("Original Data Frame: \n", df)
grouping = df.groupby("Department")["Salary"].sum()
print("Grouping Departments and compute the sum salary of each department:\n",grouping)


grouping_1 = df.groupby(["Age", "Remote_Worker"])["Salary"].sum()
print("Grouping Age and Remote_Worker: \n", grouping_1)