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
#Adding a column in our dataset.
print("Before adding column:\n", df)
df["Bonus"] = df["Salary"] * 0.15
print("=======================================================================")
print("After adding column Bonus:\n", df)

#Adding column using insert() method
print("=======================================================================")
df.insert(1, "Employee Name", ["Umar", "Nomi", "Fasih", "Saboor", "Khan", "Saif", "Tayyab", "Malak Saab"])
print("After adding column Employee Name:\n", df,)

#Modifying data in a specific cell using .loc[] method
df.loc[2, "Salary"] = 65000
print("=======================================================================")
print("After modifying salary of Fasih:\n", df)
#Modifying a multiple values of a column
print("=======================================================================")
df["Department"] = df["Department"].replace(["IT", "HR"], "SE")
print("After changing Departement of IT and HR to SE: \n", df)
#Modifying an entire column
df["Salary"] = df["Salary"] * 0.15
print("=======================================================================")
print("After updating Salary and giving all Employees an increment of 15%:\n", df)