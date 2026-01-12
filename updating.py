import pandas as pd

data = {
    "Name":['Ram','Shyam','Sita','Geeta','John','Alexa','Raj'],
    "Age":['40','20','50','60','55','66','45'],
    "Salary":[500,800,600,700,200,400,900],
    "Perfomace Score":[85,55,34,78,67,99,78]
}

df = pd.DataFrame(data)
print(df)

# .loc[]
# df.loc[row_index, "column name"] = new_value
df.loc[0, 'Salary'] = 5500
print(df)