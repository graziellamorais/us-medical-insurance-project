'''
Project Objectives:
- Work locally on your own computer
- Import a dataset into your program
- Analyze a dataset by building out functions or class methods
- Use libraries to assist in your analysis
- Optional: Document and organize your findings
- Optional: Make predictions about a dataset’s features based on your findings
'''

import numpy as np
import pandas as pd

# Importing the dataset
# Reading CSV file into a DataFrame
df = pd.read_csv('insurance.csv')

# You can now access columns directly from the DataFrame
ages = df['age']
sexes = df['sex']
bmis = df['bmi']
children = df['children']
smokers = df['smoker']
regions = df['region']
charges = df['charges']


# Basic Descriptive Analysis

# 1. How many women and how many men?
count_women = df[df['sex'] == 'female'].shape[0]
count_men = df[df['sex'] == 'male'].shape[0]

print(f'Number of women: {count_women}')
print(f'Number of men: {count_men}')
print(f'There are {count_men - count_women} more men than women.')
print('-' * 40)


# 2. Average number of children
average_children = df['children'].mean()
print(f'Average number of children: {average_children:.2f}')
print('-' * 40)


# 3. What is the average charge for each region?
average_charges_per_region = df.groupby('region')['charges'].mean()
print(average_charges_per_region)
print('-' * 40)


# 4. How does the average BMI differ between smokers and non-smokers?
average_bmi_smokers = df[df['smoker'] == 'yes']['bmi'].mean()
average_bmi_non_smokers = df[df['smoker'] == 'no']['bmi'].mean()

print(f'Average BMI for smokers: {average_bmi_smokers:.2f}')
print(f'Average BMI for non-smokers: {average_bmi_non_smokers:.2f}')
print(f'Difference between average BMI: {abs(average_bmi_smokers - average_bmi_non_smokers):.2f}')
print('-' * 40)


# 5.  What is the distribution of ages in the dataset?
# 6. What is the average age for someone who has at least one child in this dataset?




# Correlation and Relationships

# 7. Is there a correlation between BMI and charges?
correlation_bmi_charges = df['bmi'].corr(df['charges'])
print(f'Correlation between BMI and charges: {correlation_bmi_charges:.2f}')
print('-' * 40)

# How does the number of children affect insurance charges?
# Is there a significant difference in charges between smokers and non-smokers?
# Do charges vary significantly by sex?



# Regional Analysis

# Which region has the highest average charges?
# How does the number of children affect charges in each region?



# Advanced Analysis

# Can we predict charges based on age, BMI, number of children, smoking status, and region?
# What are the main factors affecting charges in the model?



# Trend Analysis
# Are there any trends in charges based on age or BMI?
# Does the region have any significant trends in charges over time (if time data is available)?



# Outlier Detection

# Are there any outliers in charges, BMI, or age?
# How do outliers impact the overall analysis of charges?



# Statistical Analysis

# What is the distribution of charges?
# What statistical tests can we perform to determine if the differences in charges between groups (e.g., smokers vs. non-smokers) are significant?



# Visualization

# How can we visualize the relationship between age and charges?
# What patterns can be identified through scatter plots or box plots of charges against different variables?



# Customer Segmentation

# Can we segment customers into groups based on their charges and demographic information?
# What are the characteristics of high-charge vs. low-charge customers?
