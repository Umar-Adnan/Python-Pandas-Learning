import pandas as pd
df = pd.read_excel("Lab work.xlsx")
# print(df.info())
df_O = pd.read_csv("online food delivery dataset.csv")
print(df_O.info())
df_custom= pd.read_json("Data set from Creating DF.json")
# print(df_custom.info())