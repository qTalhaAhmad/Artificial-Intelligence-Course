import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("dataset.csv")
print(df)

x = np.array(df['Annual_Income_(k$)'])
y = np.array(df['Spending_Score'])
plt.scatter(x, y)
plt.show()

X = df.iloc[:, [3, 4]].values

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

plt.plot(range(1, 11), wcss)
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')

y_kmeans = kmeans.fit_predict(X)
plt.show()

kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)

plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s=60, c='blue', label='Cluster2')
plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s=60, c='red', label='Cluster1')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s=60, c='green', label='Cluster3')
y_kmeans = kmeans.fit_predict(X)
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=100, c='black', label='Centroids')
plt.scatter(X[y_kmeans == 3, 0], X[y_kmeans == 3, 1], s=60, c='violet', label='Cluster4')
plt.scatter(X[y_kmeans == 4, 0], X[y_kmeans == 4, 1], s=60, c='yellow', label='Cluster5')

plt.xlabel('Annual Income (k$)')
plt.ylabel('Spending Score (1-100)')

plt.legend()
plt.show()
