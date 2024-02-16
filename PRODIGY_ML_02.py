# Creating a K-mean clustering algoorithm to group
# customers of a retail store based on their purchase
# history

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("task2\Mall_Customers.csv")
dataset = dataset.iloc[:, [3, 4]].values

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(dataset)

plt.scatter(dataset[y_kmeans == 0, 0], dataset[y_kmeans == 0, 1], s = 30, c = 'red', label = 'Cluster 1')
plt.scatter(dataset[y_kmeans == 1, 0], dataset[y_kmeans == 1, 1], s = 30, c = 'blue', label = 'Cluster 2')
plt.scatter(dataset[y_kmeans == 2, 0], dataset[y_kmeans == 2, 1], s = 30, c = 'green', label = 'Cluster 3')
plt.scatter(dataset[y_kmeans == 3, 0], dataset[y_kmeans == 3, 1], s = 30, c = 'cyan', label = 'Cluster 4')
plt.scatter(dataset[y_kmeans == 4, 0], dataset[y_kmeans == 4, 1], s = 30, c = 'magenta', label = 'Cluster 5')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s = 100, c = 'yellow', label = 'Centroids')

plt.title('Clusters of customers')
plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')
plt.legend()
plt.show()