#%%
# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Load your cleaned dataset into a DataFrame (replace 'your_dataset.csv' with your actual file path)
df = pd.read_csv('E:\Graduate\Project\DM Project\merged_data.csv')

#%%

# Display basic information about the dataset
print(df.info())

# Display summary statistics
print(df.describe())

# Check for missing values
print(df.isnull().sum())

# %%

# Histogram for 'Depression (%)'
plt.hist(df['Depression (%)'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Depression (%)')
plt.xlabel('Depression (%)')
plt.ylabel('Frequency')
plt.show()

# %%
# Boxplot for 'Depression (%)'
sns.boxplot(x=df['Depression (%)'])
plt.title('Boxplot of Depression (%)')
plt.show()

#%%

####BIVARIANT


# %%
# Define a threshold for color differentiation
threshold = 5

# Create a mask for points above and below the threshold
above_threshold = df['Depression (%)'] > threshold

# Scatter Plot with two different colors
plt.scatter(
    df.loc[above_threshold, 'Depression (%)'],
    df.loc[above_threshold, 'Alcohol use disorders (%)'],
    alpha=0.5,
    color='skyblue',  # Color for points above the threshold
    label='Above Threshold'
)

plt.scatter(
    df.loc[~above_threshold, 'Depression (%)'],
    df.loc[~above_threshold, 'Alcohol use disorders (%)'],
    alpha=0.5,
    color='coral',  # Color for points below or equal to the threshold
    label='Below Threshold'
)

plt.title('Scatter Plot: Depression (%) vs Alcohol use disorders (%)')
plt.xlabel('Depression (%)')
plt.ylabel('Alcohol use disorders (%)')
plt.legend()  # Show legend to differentiate colors
plt.show()




# %%
# Example: Select top 10 countries by count
top_countries = df['Country'].value_counts().head(10).index
sns.boxplot(x=df[df['Country'].isin(top_countries)]['Country'], y=df['Depression (%)'], palette='pastel')
plt.title('Boxplot: Top 10 Countries vs Depression (%)')
plt.xlabel('Country')
plt.ylabel('Depression (%)')
plt.xticks(rotation=45, ha='right')
plt.show()


# %%

from scipy.stats import ttest_ind

# Example data (replace with your actual data)
group_a = df[df['Alcohol use disorders (%)'] == 'A']['Depression (%)']
group_b = df[df['Drug use disorders (%)'] == 'B']['Depression (%)']

# Perform t-test
t_stat, p_value = ttest_ind(group_a, group_b)

# Compare p-value to significance level (e.g., 0.05)
alpha = 0.05
if p_value <= alpha:
    print("Reject the null hypothesis: There is a significant difference.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference.")

    #p-value > alpha (e.g., p > 0.05): Fail to reject the null hypothesis. There is not enough evidence to conclude a significant difference
    #Fail to reject the null hypothesis: There is no significant difference.


# %%


# Select specific features for the correlation matrix
selected_features = ['Schizophrenia (%)', 'Bipolar disorder (%)', 'Eating disorders (%)', 
                     'Anxiety disorders (%)', 'Drug use disorders (%)', 'Depression (%)', 
                     'Alcohol use disorders (%)']

# Create a subset DataFrame with selected features
selected_df = df[selected_features]

# Calculate correlation matrix for selected features
correlation_matrix_selected = selected_df.corr()

# Plot heatmap for selected features
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix_selected, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)
plt.title('Correlation Matrix for Selected Features')
plt.show()


# %%
# Create boxplots for selected features
plt.figure(figsize=(12, 8))
sns.boxplot(data=selected_df, palette='Set2')
plt.title('Boxplots for Selected Features')
plt.xticks(rotation=90)
plt.show()

# %%
from scipy.stats import zscore

# Calculate z-scores for 'Eating Disorders (%)'
z_scores_eating_disorders = zscore(selected_df['Eating disorders (%)'])

# Define a z-score threshold (e.g., 3)
z_threshold = 3

# Identify outliers based on the z-score threshold
outliers_eating_disorders = (z_scores_eating_disorders > z_threshold) | (z_scores_eating_disorders < -z_threshold)

# Print the indices of outliers for 'Eating Disorders (%)'
print("Indices of outliers for 'Eating Disorders (%)':")
outlier_indices_eating_disorders = selected_df.index[outliers_eating_disorders]
if len(outlier_indices_eating_disorders) > 0:
    print(f"{list(outlier_indices_eating_disorders)}")
else:
    print("No outliers")



# %%
from scipy.stats import zscore
# Calculate z-scores for 'Eating Disorders (%)'
z_scores_eating_disorders = zscore(df['Eating disorders (%)'])

# Define a z-score threshold (e.g., 3)
z_threshold = 3

# Identify outliers based on the z-score threshold
outliers_eating_disorders = (z_scores_eating_disorders > z_threshold) | (z_scores_eating_disorders < -z_threshold)

# Remove rows with outliers in 'Eating Disorders (%)'
df_no_outliers = df[~outliers_eating_disorders]

# Display the number of rows before and after removing outliers
print(f"Number of rows before removing outliers: {len(df)}")
print(f"Number of rows after removing outliers: {len(df_no_outliers)}")

# Display the DataFrame after removing outliers
print("\nDataFrame after removing outliers:")
print(df_no_outliers.head())

# %%
#Removing Ouliers in Eating Disorder
# Box plot before removing outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x=df['Eating disorders (%)'])
plt.title('Box Plot Before Removing Outliers')
plt.show()

# Box plot after removing outliers
plt.figure(figsize=(10, 6))
sns.boxplot(x=df_no_outliers['Eating disorders (%)'])
plt.title('Box Plot After Removing Outliers')
plt.show()

# Summary statistics before and after
print("\nSummary Statistics Before Removing Outliers:")
print(df['Eating disorders (%)'].describe())

print("\nSummary Statistics After Removing Outliers:")
print(df_no_outliers['Eating disorders (%)'].describe())

# %%
