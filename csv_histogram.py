import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Reading a CSV file
data = pd.read_csv('data.csv')

# 2. Displaying the first few rows of the dataframe
print("First 5 rows of the dataset:")
print(data.head())

# 3. Basic statistics
print("\nBasic statistics of the dataset:")
print(data.describe())

# 4. Data Manipulation: Adding a new column with a calculated value
data['New_Column'] = data['Existing_Column'] * np.random.random()

# 5. Handling missing values by filling them with the mean of the column
data['New_Column'].fillna(data['New_Column'].mean(), inplace=True)

# 6. Data Visualization: Histogram of the 'New_Column'
plt.figure(figsize=(10, 6))
plt.hist(data['New_Column'], bins=30, alpha=0.7, color='blue')
plt.title('Histogram of New_Column')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()