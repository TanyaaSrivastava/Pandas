import pandas as pd

data = {
    "Name":['Ram','Shyam','Ghanshyam'],
    "Age":[10,20,30],
    "City":['Nagapur',"Mumbai","Delhi"]
}

df = pd.DataFrame(data)
print(df)

#to save file in .csv method
df.to_csv("output.csv")
#save to excel
df.to_excel("output.xlsx")

df.to_json("output.json")