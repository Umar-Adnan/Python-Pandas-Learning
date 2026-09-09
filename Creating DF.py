import pandas as pd
data_frame = {
    "Name":["Umar", "Nomi", "Saboor"],
    "Age":[22,21,22],
    "City":["Lahore", "Sahiwal", "Rawalpindi"]
}

df = pd.DataFrame(data_frame) #Creating a DF
print(df)

df.to_csv("Data set from Creating DF.csv", index=False) #Saving the DF without indexes.
df.to_excel("Data set from Creating DF.xlsx", index=True)
df.to_json("Data set from Creating DF.json", index=False)
