import pandas as pd

data = {
    "Name":['Ram','Shyam','Sita','Geeta','John','Alexa','Raj'],
    "Age":['40','20','50','60','55','66','45'],
    "Salary":[500,800,600,700,200,400,900],
    "Perfomace Score":[85,55,34,78,67,99,78]
}

df = pd.DataFrame(data)
print(df)
#selecting single row
print("Nanes (Single column return series )")
name = df['Name']
print(name)

#selecting multiple columns
subset = df[["Name", "Salary"]]
print('\nSubset with Name and Salary')
print(subset)
