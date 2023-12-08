#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
df = pd.read_csv('C:/Users/gpras/Downloads/df.csv')# Assuming 'your_dataframe' is the name of your DataFrame
column_names = df.columns

# Print or display the column names
print(column_names)


# #  1. Prevalent patterns of comorbidity between depression and alcohol use disorders globally

# In[2]:


plt.figure(figsize=(12, 6))
sns.scatterplot(x='Depression(%)', y='Alcoholusedisorders(%)', data=df, hue='Country', palette='viridis')
plt.title('Prevalent Patterns of Comorbidity: Depression vs Alcohol Use Disorders')
plt.xlabel('Depression (%)')
plt.ylabel('Alcohol Use Disorders (%)')
plt.legend(bbox_to_anchor=(1, 1))
plt.show()


# In[3]:


plt.figure(figsize=(12, 8))
sns.heatmap(df[['Depression(%)', 'Anxietydisorders(%)', 'Alcoholusedisorders(%)', 'Drugusedisorders(%)']].corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Among Mental Health Variables')
plt.show()


# In[4]:


# Box Plot: Distribution of Depression Rates
plt.figure(figsize=(10, 6))
sns.boxplot(y='Depression(%)', data=df, palette='pastel')
plt.title('Distribution of Depression Rates')
plt.ylabel('Depression Rate')
plt.show()


# In[5]:


# 3. Box Plot: Distribution of Depression Rates by Gender
plt.figure(figsize=(10, 6))
sns.boxplot(x='Year', y='Depression(%)', data=df, palette='pastel')
plt.title('Distribution of Depression Rates by Gender')
plt.xlabel('Gender')
plt.ylabel('Depression Rate')
plt.show()


# # 2. Trend in the probability of dying between ages 30 and 70 from cardiovascular disease, cancer, diabetes, and chronic respiratory disease over the past decade

# In[6]:


plt.figure(figsize=(12, 6))
df[['Year', 'Dying_both', 'Dying_m', 'Dying_f']].groupby('Year').mean().plot(marker='o')
plt.title('Trend in Probability of Dying (Ages 30-70)')
plt.xlabel('Year')
plt.ylabel('Probability (%)')
plt.legend(['Both Sexes', 'Male', 'Female'])
plt.show()


# In[7]:


plt.figure(figsize=(12, 6))
df[['Year', 'Dying_m', 'Dying_f']].groupby('Year').mean().plot(marker='o')
plt.title('Trend in Probability of Dying (Ages 30-70)')
plt.xlabel('Year')
plt.ylabel('Probability (%)')
plt.legend(['Male', 'Female'])
plt.show()


# # 3. Are men or women more likely to suffer from mental health disorders?

# In[8]:


# 2. Bar Plot: Comparison of Mental Health Disorders 
plt.figure(figsize=(12, 6))
df[['Anxietydisorders(%)', 'Depression(%)', 'Alcoholusedisorders(%)', 'Drugusedisorders(%)']].mean().plot(kind='bar', color=['blue', 'orange', 'green', 'red'])
plt.title('Comparison of Mental Health Disorders')
plt.ylabel('Percentage')
plt.show()


# # 4. Which type of mental disorder is linked with suicide most?

# In[9]:


plt.figure(figsize=(12, 6))
df[['Schizophrenia(%)', 'Bipolardisorder(%)', 'Eatingdisorders(%)', 'Anxietydisorders(%)', 'Drugusedisorders(%)', 'Depression(%)', 'Alcoholusedisorders(%)', 'Suicide']].mean().sort_values().plot(kind='barh', color='purple')
plt.title('Association of Mental Disorders with Suicide')
plt.xlabel('Percentage')
plt.show()


# In[10]:


# 4. Pair Plot: Explore Relationships between Variables
sns.pairplot(df[['Depression(%)', 'Anxietydisorders(%)', 'Alcoholusedisorders(%)', 'Suicide']], diag_kind='kde')
plt.suptitle('Pair Plot of Mental Health Variables', y=1.02)
plt.show()


# In[11]:


import plotly.express as px

# Choropleth map for Depression rates globally
fig = px.choropleth(df, 
                    locations="Country", 
                    locationmode='country names', 
                    color="Depression(%)", 
                    title="Global Depression Rates",
                    color_continuous_scale=px.colors.sequential.Plasma)

# Show the figure
fig.show()


# In[12]:


# Scatter plot for comorbidity patterns
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Depression(%)', y='Alcoholusedisorders(%)', data=df, hue='Country', palette="viridis", s=100)
plt.title('Global Comorbidity Patterns: Depression and Alcohol Use Disorders')
plt.xlabel('Depression (%)')
plt.ylabel('Alcohol Use Disorders (%)')
plt.grid(True)
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


# In[13]:


# 1. Line Plot: Trend in Suicide Rates Over Time
plt.figure(figsize=(12, 6))
df[['Year', 'Suicide']].groupby('Year').mean().plot(marker='o')
plt.title('Trend in Suicide Rates Over Time')
plt.xlabel('Year')
plt.ylabel('Suicide Rate')
plt.show()


# In[ ]:




