import pandas as pd

data = {
    "Name":['Ram','Shyam','Sita','Geeta','John','Alexa','Raj'],
    "Age":[40,20,50,60,55,66,45],
    "Salary":[500,800,600,700,200,400,900],
    "Perfomace Score":[85,55,34,78,67,99,78]
}

df = pd.DataFrame(data)
print(df)


#single filtering
high_salary = df[df['Salary']>400]
print('employess with salary >400')
print(high_salary)


#multiple filtering
filtered = df[(df['Age'] > 50) & (df['Salary'] > 500)]

print("Employee list: Age > 30 and Salary > 500")
print(filtered)

#using or condition
filtered_or = df[(df['Age'] > 50) | (df['Perfomace Score'] > 55)]

print("Employee list: Age > 30 and perfomace score > 55")
print(filtered_or)