import pandas as pd

# Reading the CSV files using raw strings
items_df = pd.read_csv(r'C:\Users\Rohit_Rawat\Documents\aays-training\training-aays\python_training\items.csv')
sales_df = pd.read_csv(r'C:\Users\Rohit_Rawat\Documents\aays-training\training-aays\python_training\sales.csv')

print(items_df.head(2))
print(sales_df.head(2))

#Merging the two dataframes on common column 'ItemId'
merged_df = pd.merge(items_df, sales_df, on = 'ItemId', how = 'inner')

print(merged_df.head(5))

#Creating new columns and aggregating the TotalRevenue and NumSales
merged_df['TotalRevenue'] = merged_df['Price'] * merged_df['NumSales']

merged_df = merged_df.groupby('ItemId')[['NumSales', 'TotalRevenue']].sum().reset_index().rename(columns={'NumSales': 'TotalUnitsSold', 'TotalRevenue': 'RevenueGenerated'})

merged_df['AvgCost'] = merged_df['RevenueGenerated'] / merged_df['TotalUnitsSold']

print(merged_df.head)


