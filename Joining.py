import pandas as pd

# DataFrames using Emp_ID as the index
df_personal_info = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}, index=[101, 102, 103])

df_employment_info = pd.DataFrame({
    'Department': ['IT', 'HR', 'Finance'],
    'Salary': [60000, 75000, 90000]
}, index=[101, 102, 104])  # Note: 103 vs 104 index mismatch

print("=== 1. Default Left Join on Indexes ===")
# Keeps index 101, 102, 103 from the left DataFrame
print(df_personal_info.join(df_employment_info, how='left'))

print("\n=== 2. Inner Join on Indexes ===")
# Keeps only indexes present in both (101, 102)
print(df_personal_info.join(df_employment_info, how='inner'))