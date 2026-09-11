import pandas as pd

# Setup DataFrames
df_employees = pd.DataFrame({
    'Emp_ID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Dept_ID': ['D1', 'D2', 'D1', 'D4']  # D4 has no match in departments
})

df_departments = pd.DataFrame({
    'Dept_ID': ['D1', 'D2', 'D3'],      # D3 has no employees
    'Dept_Name': ['IT', 'HR', 'Finance']
})

print("=== 1. INNER JOIN (Only exact matches: D1, D2) ===")
print(pd.merge(df_employees, df_departments, on='Dept_ID', how='inner'))

print("\n=== 2. LEFT JOIN (All employees + matched depts) ===")
print(pd.merge(df_employees, df_departments, on='Dept_ID', how='left'))

print("\n=== 3. RIGHT JOIN (All depts + matched employees) ===")
print(pd.merge(df_employees, df_departments, on='Dept_ID', how='right'))

print("\n=== 4. OUTER JOIN (All employees and all depts) ===")
print(pd.merge(df_employees, df_departments, on='Dept_ID', how='outer'))