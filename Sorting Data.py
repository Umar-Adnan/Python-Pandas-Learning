import pandas as pd
import numpy as np

# Sample dataset representing employee records
data = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Age': [25, 34, 29, 42, 29, 38, np.nan, 29],
    'Salary': [50000, 72000, 61000, 110000, 58000, 85000, 92000, 61000],
    'Department': ['IT', 'HR', 'IT', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
    'Remote_Worker': [True, False, True, False, True, False, True, True]
}

df = pd.DataFrame(data)

#Sorting Salary and Age in a ascending order

df = df.sort_values(by = ["Salary", "Age"], ascending=[False, False])
print(df)