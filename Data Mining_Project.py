#!/usr/bin/env python
# coding: utf-8

# In[55]:


import pandas as pd

# Load the datasets
df1 = pd.read_csv('Data.csv')
df2 = pd.read_csv('Mental health Depression disorder Data.csv')


# In[56]:


print(type(df2['Year']))
print(df2['Year'].head())


# In[57]:


print(df2['Year'].isnull().sum())


# In[59]:


import pandas as pd

df1 = pd.read_csv('Data.csv')
df2 = pd.read_csv('Mental health Depression disorder Data.csv')

# Merge DataFrames on the 'Country' and 'Year' columns
merged_df = pd.merge(df1, df2, on=['Country', 'Year'], how='inner')

# Display the merged DataFrame
print(merged_df)

merged_df.to_csv('C:/Users/gpras/OneDrive/Desktop/merged_dataset.csv', index=False)


# In[61]:


# Data Cleaning
# Handling missing values
merged_df.fillna(method='ffill', inplace=True)  # Forward fill

# Drop rows with missing values
merged_df.dropna(inplace=True)

# Fill missing values with zero
merged_df.fillna(0, inplace=True)

# Alternatively, you can use: merged_df.fillna(merged_df.mean(), inplace=True) for mean imputation

# Removing duplicates
merged_df.drop_duplicates(inplace=True)

# Data type conversions (example: converting a column to float)
# merged_df['SomeColumn'] = merged_df['SomeColumn'].astype(float)

# Outlier detection and handling (example: using IQR)
Q1 = merged_df.quantile(0.25)
Q3 = merged_df.quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR
merged_df = merged_df[~((merged_df < lower_bound) | (merged_df > upper_bound)).any(axis=1)]

# Save the cleaned dataset
print(merged_df)
merged_df.to_csv('C:/Users/gpras/OneDrive/Desktop/merged_dataset.csv', index=False)


# In[ ]:




