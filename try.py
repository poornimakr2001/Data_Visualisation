# -*- coding: utf-8 -*-
"""try.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TMqlUwFDOZ6BhQKwANKjfVkAq4X-UAba
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Path to your CSV file in Google Drive
file_path = '/content/drive/MyDrive/flights.csv'

# Load CSV data into a DataFrame
df = pd.read_csv(file_path)

# Display the first few rows to understand the structure
print(df.head())

# Calculate correlations if needed (example)
correlation_matrix = df.corr()

# Plot heatmap using seaborn
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()

import pandas as pd

# Example data (replace with your actual DataFrame)
data = {
    'id': [0, 1, 2, 3, 4],
    'year': [2013, 2013, 2013, 2013, 2013],
    'month': [1, 1, 1, 1, 1],
    'day': [1, 1, 1, 1, 1],
    'dep_time': [517.0, 533.0, 542.0, 544.0, 554.0],
    'sched_dep_time': [515, 529, 540, 545, 600],
    'dep_delay': [2.0, 4.0, 2.0, -1.0, -6.0],
    'arr_time': [830.0, 850.0, 923.0, 1004.0, 812.0],
    'sched_arr_time': [819, 830, 850, 1022, 837],
    'arr_delay': [11.0, 20.0, 33.0, -18.0, -25.0],
    'flight': [1545, 1714, 1141, 725, 461],
    'air_time': [227.0, 227.0, 160.0, 183.0, 116.0],
    'distance': [1400, 1416, 1089, 1576, 762],
    'hour': [5, 5, 5, 5, 6],
    'minute': [15, 29, 40, 45, 0],
    'time_hour': ['2013-01-01 05:00:00', '2013-01-01 05:00:00', '2013-01-01 05:00:00',
                  '2013-01-01 05:00:00', '2013-01-01 06:00:00'],
    'name': ['United Air Lines Inc.', 'United Air Lines Inc.', 'American Airlines Inc.',
             'JetBlue Airways', 'Delta Air Lines Inc.']
}

df = pd.DataFrame(data)

# Select numeric columns
numeric_cols = ['dep_time', 'sched_dep_time', 'dep_delay', 'arr_time', 'sched_arr_time',
                'arr_delay', 'flight', 'air_time', 'distance', 'hour', 'minute']
numeric_df = df[numeric_cols]

# Calculate correlations
correlation_matrix = numeric_df.corr()

# Plot heatmap
import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Heatmap')
plt.show()