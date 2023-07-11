# Question 10b
# Write a program to develop Linear Discriminant Analysis (LDA) algorithms
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


class LDA:
    def __init__(self, n_components=None):
        self.n_components = n_components
        self.eig_vectors = None

    def transform(self, X, y):
        height, width = X.shape
        unique_classes = np.unique(y)
        num_classes = len(unique_classes)

        scatter_t = np.cov(X.T) * (height - 1)
        scatter_w = 0
        for i in range(num_classes):
            class_items = np.flatnonzero(y == unique_classes[i])
            scatter_w = scatter_w + \
                np.cov(X[class_items].T) * (len(class_items) - 1)

        scatter_b = scatter_t - scatter_w
        _, eig_vectors = np.linalg.eigh(
            np.linalg.pinv(scatter_w).dot(scatter_b))
        pc = X.dot(eig_vectors[:, ::-1][:, :self.n_components])

        return pc


data = pd.read_csv('./Iris.csv')
X = np.array(data.drop('species', axis=1))
y = data['species']
y = LabelEncoder().fit_transform(y)

lda = LDA(2)
X_projected = lda.transform(X, y)

print("Original Data Size:", X.shape, "\nModified Data Size:", X_projected.shape)

x1 = X_projected[:, 0]
x2 = X_projected[:, 1]

plt.scatter(x1, x2, c=y, edgecolor="none", alpha=0.8,
            cmap=plt.cm.get_cmap("viridis", 3))
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.colorbar()
plt.show()
