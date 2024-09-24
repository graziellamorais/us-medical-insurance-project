'''
Project Objectives:
- Work locally on your own computer
- Import a dataset into your program
- Analyze a dataset by building out functions or class methods
- Use libraries to assist in your analysis
- Optional: Document and organize your findings
- Optional: Make predictions about a dataset’s features based on your findings
'''

import csv
import numpy as np
import pandas as pdpip

# Importing the dataset

# Openning the CSV file in read mode
with open('insurance.csv', newline='') as csvfile:
    # Creating a CSV reader object
    #reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    
    # Reading and printing each row
    #for row in reader:
    #    print(', '.join(row))
    reader = csv.DictReader(csvfile)

    # Saving columns by storing them in variables
    ages = []
    sexes = []
    bmis = []
    children = []
    smokers = []
    regions = []
    charges = []

    for row in reader:
        try:
            # Append valid data to the lists
            ages.append(row['age'])
            sexes.append(row['sex'])
            bmis.append(row['bmi'])
            children.append(int(row['children']))
            smokers.append(row['smoker'])
            regions.append(row['region'])
            charges.append(float(row['charges']))
        except ValueError as e:
            # Print a warning message for invalid data
            print(f"Warning: Skipping row due to invalid data: {e}")


# Basic Descriptive Analysis

# How many women and how many men?

def count_sexes(sex):
    count = sexes.count(sex)
    return count

count_women = count_sexes('female')
count_men = count_sexes('male')

# Testing
print(f'Number of women: {count_women}')
print(f'Number of men: {count_men}')
print(f'There are {count_men - count_women} more men than women.')

print('-' * 40)


# Average number of children

def calculate_average_children(children):
    total_children = sum(children)
    number_of_entries = len(children)
    # Avoid division by zero
    if number_of_entries == 0:
        return 0
    average_children = total_children / number_of_entries
    return average_children

# Testing
average_children = calculate_average_children(children)
print(f'Average number of children: {average_children:.2f}')

print('-' * 40)


# What is the average charge for each region?

def calculate_average_charges_per_region(regions, charges):
    # Check if lengths of regions and charges match
    if len(regions) != len(charges):
        print(f"Warning: Mismatch in data length. Regions: {len(regions)}, Charges: {len(charges)}")
        return None

    charges_per_region = {}
    region_counts = {}

    # Populating the dictionaries
    for region, charge in zip(regions, charges):
        if region in charges_per_region:
            charges_per_region[region] += charge
            region_counts[region] += 1
        else:
            charges_per_region[region] = charge
            region_counts[region] = 1

    # Calculating and printing average charges per region
    average_charges = {}
    for region in charges_per_region:
        average_charges[region] = charges_per_region[region] / region_counts[region]
        print(f'Average charge for {region}: ${average_charges[region]:.2f}')

    return average_charges

# Testing
avg_charges_per_region = calculate_average_charges_per_region(regions, charges)

print('-' * 40)

# Accessing a specific region's average charge
specific_region = 'southwest'
if avg_charges_per_region and specific_region in avg_charges_per_region:
    print(f"Average charge for {specific_region}: ${avg_charges_per_region[specific_region]:.2f}")
else:
    print(f"{specific_region} is not found in the region list.")

print('-' * 40)


# How does the average BMI differ between smokers and non-smokers?

def calculate_average_bmi_by_smoking_status(bmis, smokers):
    # Separating smokers and non-smokers
    smoker_bmis = []
    non_smoker_bmis = []

    # Iterating through zipped bmis and smokers lists
    for bmi, smoker in zip(bmis, smokers):
        # If it's a smoker, add their bmi to the smoker_bmis list
        if smoker == 'yes':
            smoker_bmis.append(float(bmi)) # Converting to float
        # Otherwise, add it to the non_smoker_bmis list
        else:
            non_smoker_bmis.append(float(bmi))
    
    # Calculating average BMI for smokers, handling cases where there may be no smokers in the dataset
    avg_bmi_smokers = sum(smoker_bmis) / len(smoker_bmis) if smoker_bmis else 0

    # Calculating average BMI for non-smokers, handling cases where there may be no non-smoker in the dataset
    avg_bmi_non_smokers = sum(non_smoker_bmis) / len(non_smoker_bmis) if non_smoker_bmis else 0

    return avg_bmi_smokers, avg_bmi_non_smokers

# Testing
avg_bmi_smokers, avg_bmi_non_smokers = calculate_average_bmi_by_smoking_status(bmis, smokers)

print(f'Average BMI for smokers: {avg_bmi_smokers:.2f}')
print(f'Average BMI for non-smokers: {avg_bmi_non_smokers:.2f}')
print(f'Difference between average BMI: {abs(avg_bmi_smokers - avg_bmi_non_smokers):.2f}') # Using the abs() function to ensure the result is always positive
        
print('-' * 40)

# What is the distribution of ages in the dataset?
# What is the average age for someone who has at least one child in this dataset?




# Correlation and Relationships

# Is there a correlation between BMI and charges?
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
