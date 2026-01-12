"""types of aggregation function
1-sum()
2-mean()
3-count()
4-min()
5-max()
6-std()
"""

import pandas as pd

data = { 
    "Name":['Arun','Varun','Karun','narun','marun'],
    "Age":[28,34,22,34,44],
    "Salary":[10000,20000,50000,90000,80000]
}
df = pd.DataFrame(data)
#single column
#grouped = df.groupby("Age")["Salary"].sum()
#print(grouped)

#multiple column
grouped = df.groupby(["Age","Name"])["Salary"].sum()
print(grouped)