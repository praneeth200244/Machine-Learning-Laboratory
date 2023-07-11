# Question no 8
# Write a program to perform unsupervised K-means clustering techniques on Iris dataset.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def kmeans(X, K, max_iters=100):
    centroids = X[:K]

    for _ in range(max_iters):
        labels = np.argmin(np.linalg.norm(
            X[:, np.newaxis] - centroids, axis=2), axis=1)
        new_centroids = np.array(
            [X[labels == k].mean(axis=0) for k in range(K)])

        if np.all(centroids == new_centroids):
            break
        centroids = new_centroids

    return labels, centroids


data = pd.read_csv('Iris.csv')
X = data.drop('species', axis=1).values

K = 3
labels, centroids = kmeans(X, K)

print("Labels:", labels)
print("Centroids:", centroids)

plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red', s=200)
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.title('K-means Clustering of Iris Dataset')
plt.show()
