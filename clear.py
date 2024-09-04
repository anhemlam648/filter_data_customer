import pandas as pd

# For example data 
data = {'name': ['Nghia', 'Duy', 'Tấn'], 'age': [22, 22, 25], 'service': [14, 25, 12]}

export = pd.DataFrame(data)

#read file excel
# export = pd.read_excel('data_customer.xlsx')

# print(export)

#show info
# print(export.info())

#show describe
# print(export.describe())

#filter customer
# filtered = export[export['age'] > 22]
filterservice = export[export['service'] > 20]

# print(filtered)
print(filterservice)

# Export data to Excel file
filtered.to_excel('processed.xlsx', index=False)

# Export data to CSV file
filtered.to_csv('processed.csv', index=False)