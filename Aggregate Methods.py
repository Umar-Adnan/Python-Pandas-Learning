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

print("--- Original DataFrame ---")
print(df)
print("\n" + "="*60 + "\n")

# Built-in Aggregations (Single Column / Entire DF)

print("--- 1. Single Column Aggregations ---")
print("Mean Salary:     ", df['Salary'].mean())
print("Median Age:      ", df['Age'].median())
print("Salary Std Dev:  ", df['Salary'].std())
print("Total Salary Sum:", df['Salary'].sum())
print("Min / Max Age:   ", df['Age'].min(), "/", df['Age'].max())
print("Count (Non-NaN): ", df['Department'].count())  # Ignores NaNs
print("Size (Total):    ", df['Department'].size)   # Includes NaNs
print("Mode Dept:       ", df['Department'].mode()[0])

print("\n" + "="*60 + "\n")
