import pandas as pd

df_customers = pd.DataFrame({
    'CustomerID':[1,2,3],
    'Name':['Ramesh','Suresh','Kalpesh']
})
#order frames
df_orders = pd.DataFrame({
    'CustomerID':[1,2,4],
    'OrderAmount':[250,800,300]
})

#merge
df_merge = pd.merge(df_customers,df_orders, on="CustomerID",how = "inner")
print('inner join')
print(df_merge)