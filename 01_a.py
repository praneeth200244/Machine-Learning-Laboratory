# Question 1a
# Visualize the n-dimensional data using 3D surface plots.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv('ToyotaCorolla.csv')
dataset.head(5)

x = dataset['KM'][:100]
y = dataset['Age'][:100]
z = dataset['Price'][:100]

# %matplotlib notebook
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')
ax.plot_trisurf(x, y, z)
