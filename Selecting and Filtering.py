import pandas as pd

df = pd.read_csv("Sample Dataset.csv")
print("The complete sample dataset: \n", df)
print("===================================================================")

E_id = df["Employee_ID"]
print("Extracting only Employee ID: \n", E_id)
print("===================================================================")

subset = df[["Employee_ID", "Age", "Salary" ]] #Returns only the mentioned columns
print("Extracting Employee ID, Age and Salary for the complete Dataset:\n", subset)
print("===================================================================")

filter_1 = df[df["Age"] > 30] #Returns all records with employees having age greater than 30
print("Filtering age greater than 30:\n", filter_1)
print("===================================================================")

filter_2 = df[(df["Age"] > 30) & (df["Salary"] > 60000)] #Returns all records that are true for the specified conditions, any logical operator or condional logic can be used to filter data.
print("Filtering age greater than 30 and salary greater than 60000:\n", filter_2)
