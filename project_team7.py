import pandas as pd

# Load the datasets
df1 = pd.read_csv('data.csv')
df2 = pd.read_csv('Mental health Depression disorder Data.csv')

# Get the needed part from the whole dataset
df2 = df2.iloc[0:6468]

# Preparation for merging
df2 = df2.rename(columns={"Entity":"Country"})
print(df1.dtypes)
print(df2.dtypes)
df2["Year"]=df2["Year"].astype("int")

# Merge DataFrames on the 'Country' and 'Year' columns
merged_df = pd.merge(df2, df1, on=['Country', "Year"], how='inner')
# Display the merged DataFrame
print(merged_df)

merged_df.to_csv('merged_data.csv', index=False)
'''
'Both sexes' means 'Probability (%) of dying between age 30 and exact age 70 from any of cardiovascular disease, cancer, diabetes, or chronic respiratory disease for both sexes'
'Male' means 'Probability (%) of dying between age 30 and exact age 70 from any of cardiovascular disease, cancer, diabetes, or chronic respiratory disease for male'
'Female' means 'Probability (%) of dying between age 30 and exact age 70 from any of cardiovascular disease, cancer, diabetes, or chronic respiratory disease for female'
'Both sexes.1' means 'Crude suicide rates (per 100 000 population) for both sexes'
'Male.1' means 'Crude suicide rates (per 100 000 population) for male'
'Female.1' means 'Crude suicide rates (per 100 000 population) for female'
'''
