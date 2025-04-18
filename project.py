# COVID-19 Data Analysis Project
# Author: Your Name
# University: Silver Oak University
# Description: This script uses Pandas and Matplotlib to analyze sample COVID-19 data
#              for multiple countries and generate visual insights.

# -------------------- Step 1: Import Required Libraries --------------------
import pandas as pd
import matplotlib.pyplot as plt

# -------------------- Step 2: Create Sample Dataset ------------------------
# This is a simulated dataset representing COVID-19 statistics.
data = {
    'Country': ['USA', 'India', 'Brazil', 'Russia', 'UK'],
    'Total Cases': [34000000, 31000000, 19000000, 6000000, 5000000],
    'Total Deaths': [609000, 410000, 530000, 150000, 130000],
    'Total Recovered': [28000000, 30000000, 17000000, 5800000, 4800000]
}

# Convert the dictionary to a Pandas DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("=== COVID-19 Dataset ===")
print(df)

# -------------------- Step 3: Calculate Additional Insights -----------------
# Add two new columns: Death Rate and Recovery Rate
df['Death Rate (%)'] = (df['Total Deaths'] / df['Total Cases']) * 100
df['Recovery Rate (%)'] = (df['Total Recovered'] / df['Total Cases']) * 100

print("\n=== Dataset with Rates ===")
print(df)

# -------------------- Step 4: Visualizations using Matplotlib ----------------

# Visualization 1: Total Cases by Country
plt.figure(figsize=(10, 6))
plt.bar(df['Country'], df['Total Cases'], color='skyblue')
plt.title('COVID-19 Total Cases by Country')
plt.xlabel('Country')
plt.ylabel('Total Cases')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('covid_total_cases.png')
plt.show()

# Visualization 2: Death Rate by Country
plt.figure(figsize=(10, 6))
plt.bar(df['Country'], df['Death Rate (%)'], color='red')
plt.title('COVID-19 Death Rate (%) by Country')
plt.xlabel('Country')
plt.ylabel('Death Rate (%)')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('covid_death_rate.png')
plt.show()

# Visualization 3: Recovery Rate by Country
plt.figure(figsize=(10, 6))
plt.bar(df['Country'], df['Recovery Rate (%)'], color='green')
plt.title('COVID-19 Recovery Rate (%) by Country')
plt.xlabel('Country')
plt.ylabel('Recovery Rate (%)')
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('covid_recovery_rate.png')
plt.show()

# -------------------- Step 5: Conclusion ---------------------
print("\n=== Summary ===")
print("USA has the highest number of total cases.")
print("India has the highest recovery rate among the sample countries.")
print("Death and recovery rates vary across different countries.")

# -------------------- END OF PROJECT -------------------------