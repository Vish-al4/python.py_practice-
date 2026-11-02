import pandas as pd
employees = pd.DataFrame({
    'Employee_ID': [101, 102, 103],
    'Name': ['Amit', 'Priya', 'Rahul'],
    'Age': [25, 30, 28],
    'Department': ['HR', 'IT', 'Finance'],
    'Salary': [35000, 50000, 45000]
})

print(employees[['Name', 'Salary']])

print(employees[['Age','Department']])

print(employees[employees["Department"]=="IT"])

print(employees.sort_values(by="Salary",ascending=False))

print(
    employees.groupby("Department")["Salary"].mean() 
)

v= employees.groupby("Department")["Salary"].mean()
print(v[v>35000 ])
employees.loc[
    employees["Employee_ID"] == 102, "Salary"
] = 20000

print(employees)
