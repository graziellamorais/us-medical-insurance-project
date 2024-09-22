# Medical Insurance Cost Analysis

This project analyzes a dataset containing medical insurance costs using Python. It involves data exploration, analysis, and some predictive modeling to understand factors affecting insurance charges. The dataset includes age, sex, BMI, number of children, smoking status, region, and charges.

## Project Objectives
- Import and analyze the dataset locally
- Build out functions to perform specific analyses
- Use Python libraries such as `csv`, `numpy`, and `matplotlib` for data analysis and visualization
- Optionally, make predictions based on the dataset's features using linear regression


## Dataset
The dataset used in this project (`insurance.csv`) contains the following columns:
- `age`: The age of the individual
- `sex`: Gender of the individual (male/female)
- `bmi`: Body Mass Index, a measure of body fat based on height and weight
- `children`: Number of children covered by the insurance
- `smoker`: Whether the individual is a smoker (yes/no)
- `region`: The individual's residential region (northeast, northwest, southeast, southwest)
- `charges`: Medical insurance charges billed to the individual


## Features and Analysis

1. **Basic Analysis:**
   - Count of male and female individuals in the dataset
   - Average number of children
   - Average medical insurance charge for each region
   - Average BMI difference between smokers and non-smokers
   - Age distribution and average age for individuals with children

2. **Correlation and Relationships:**
   - Correlation between BMI and charges
   - How the number of children affects insurance charges
   - Differences in charges based on smoking status and sex

3. **Advanced Analysis:**
   - Regional analysis to compare charges
   - Predictive modeling using linear regression to estimate charges based on age, BMI, number of children, smoking status, and region

4. **Outlier Detection:**
   - Identifying outliers in age, BMI, and charges
   - Analysis of the impact of outliers on the overall dataset

5. **Statistical Tests:**
   - T-tests to compare charges between smokers and non-smokers
