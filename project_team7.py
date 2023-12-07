import pandas as pd

# Load the datasets
df1 = pd.read_csv('data.csv', header=1)
df2 = pd.read_csv('Mental health Depression disorder Data.csv')

# Drop unneeded column
df2 = df2.drop("index", axis=1)

# Get the needed part from the whole dataset
df3 = df2.iloc[54276:102084,0:6]
df2 = df2.iloc[0:6468]
df3.to_csv('Suicide_rate.csv', header=None)
df3 = pd.read_csv("Suicide_rate.csv")
df3 = df3.drop("54276", axis=1)

# Preparation for merging
df2 = df2.rename(columns={"Entity":"Country"})
print(df1.dtypes)
print(df2.dtypes)
df2["Year"]=df2["Year"].astype("int")
df3.dtypes
df3 = df3[df3["Year"].isin(["2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017"])]
df3["Year"]=df3["Year"].astype("int")

# Cleaning
# Change columns names and datatypes
df1 = df1.rename(columns={"Both sexes":"Dying_both", "Male":"Dying_m", "Female":"Dying_f", "Both sexes.1":"Suicide_both", "Male.1":"Suicide_m", "Female.1":"Suicide_f"})
df2.columns = df2.columns.str.replace("\s+", "")
df3 = df3.rename(columns={"Entity":"Country", "Suicide rate (deaths per 100,000 individuals)":"Suicide", "Depressive disorder rates (number suffering per 100,000)":"Depressive"})

# Merge DataFrames on the 'Country' and 'Year' columns
merged_df = pd.merge(df2, df1, on=['Country', "Year"], how='inner')
merged_df = pd.merge(merged_df, df3[["Country","Year","Suicide"]], on=['Country', "Year"], how='inner')
# Display the merged DataFrame
print(merged_df)

# Cleaning
# Handle the values of columns
merged_df['Dying_both'] = merged_df['Dying_both'].replace(to_replace='\[[^)]*\]', value='', regex=True)
merged_df['Dying_m'] = merged_df['Dying_m'].replace(to_replace='\[[^)]*\]', value='', regex=True)
merged_df['Dying_f'] = merged_df['Dying_f'].replace(to_replace='\[[^)]*\]', value='', regex=True)
merged_df['Suicide_both'] = merged_df['Suicide_both'].replace(to_replace='\[[^)]*\]', value='', regex=True)
merged_df['Suicide_m'] = merged_df['Suicide_m'].replace(to_replace='\[[^)]*\]', value='', regex=True)
merged_df['Suicide_f'] = merged_df['Suicide_f'].replace(to_replace='\[[^)]*\]', value='', regex=True)


merged_df.to_csv('merged_data.csv', index=False)
'''
'Dying_both' means 'Probability (%) of dying between age 30 and exact age 70 from any of cardiovascular disease, cancer, diabetes, or chronic respiratory disease for both sexes'
'Dying_m' means 'Probability (%) of dying between age 30 and exact age 70 from any of cardiovascular disease, cancer, diabetes, or chronic respiratory disease for male'
'Dying_f' means 'Probability (%) of dying between age 30 and exact age 70 from any of cardiovascular disease, cancer, diabetes, or chronic respiratory disease for female'
'Suicide_both' means 'Crude suicide rates (per 100 000 population) for both sexes'
'Suicide_m' means 'Crude suicide rates (per 100 000 population) for male'
'Suicide_f' means 'Crude suicide rates (per 100 000 population) for female'
'Suicide' means 'Suicide rate (deaths per 100,000 individuals)'
'''
