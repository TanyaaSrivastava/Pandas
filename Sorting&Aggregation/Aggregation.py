"""df["column name].mean()
df["column name"].sum()
df["column name"].min()
df["column name].maz()"""

import pandas as pd
data = { 
    "Name":['Arun','Varun','Karun'],
    "Age":[28,34,22],
    "Salary":[10000,20000,50000]
}
df = pd.DataFrame(data)
avg_salary = df['Salary'].mean()
print(avg_salary)