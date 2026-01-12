import pandas as pd

data = {
    "Name":['Ram','Shyam','Sita','Geeta','John','Alexa','Raj'],
    "Age":['40','20','50','60','55','66','45'],
    "Salary":[500,800,600,700,200,400,900],
    "Perfomace Score":[85,55,34,78,67,99,78]
}

df = pd.DataFrame(data)
print(df)

df["Bonus"] = df['Salary'] * 0.1
print(df)

#using insert()
#df.insert(loc, "column_name", "same_data")
df.insert(0, "Employee ID", [10,20,30,40,50,60,70])
print(df)