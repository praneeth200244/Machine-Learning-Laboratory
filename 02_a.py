# Question 2a on Toyota Dataset
# Visualize the n-dimensional data using contour plots.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Toyota.csv')
dataset.head(5)

x = dataset['Age']
y = dataset['KM']
z = dataset['Price']

# Create a contour plot
plt.tricontourf(x, y, z, levels=20, cmap='jet')
plt.colorbar(label='Price')
plt.xlabel('Age')
plt.ylabel('KM')
plt.title('\nContour Plot of Price vs. Age and KM\n')
plt.show()
