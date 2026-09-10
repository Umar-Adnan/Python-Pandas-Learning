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
print("DataFrame:\n", df) #prints original DF.
print("================================================================")
print("Missing Data:\n", df.isnull()) #prints true/false grid of missing values.
print("================================================================")
print("Count of missing values in each Column:\n", df.isnull().sum())#prints the count of missing values in each column.
