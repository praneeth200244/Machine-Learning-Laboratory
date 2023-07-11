
# Question 4a
# Visualize the n-dimensional data using Box-plot.
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV
data = pd.read_csv('Toyota.csv').dropna()

fueltype = data['FuelType'].unique()

sns.boxplot(x=data["FuelType"], y=data['Price'])
plt.xticks(range(len(fueltype)), fueltype)

plt.show()
