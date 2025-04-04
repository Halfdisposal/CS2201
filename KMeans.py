import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
import time
import math

path = "data.csv"
df = pd.read_csv(path)
X = df[['Feature2', 'Feature3']].values
X += 10 * np.random.rand(*X.shape)
cluster_range = range(1, len(X[:, 0]))
wcss = []

for cluster in cluster_range:
    kmeans = KMeans(n_clusters = cluster, init = 'k-means++', random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
def calc_elbow(wcss):
    angle = 180
    for i in range(0, len(wcss) - 2):
        p1 = wcss[i]
        p2 = wcss[i + 1]
        p3 = wcss[i + 2]
        v1 = (1 + (p2 - p1)**2)**0.5
        v2 = (1 + (p3 - p2)**2)**0.5
        val = (-1-(p2 - p1)*(p3 - p2))/(v1*v2)
        theta = math.acos(val) * 180 / math.pi
        if theta < angle:
            angle = theta     
            return p3
        else:
            return None
            
           

def train(data):
    wcss = []
    for cluster in cluster_range:
        kmeans = KMeans(n_clusters = cluster, init = 'k-means++', random_state = 0)
        kmeans.fit(X)
        wcss.append(kmeans.inertia_)
    elbow = calc_elbow(wcss)
    idx = wcss.index(elbow) + 1
    kmeans_train = KMeans(n_clusters = idx, random_state = 42)
    print(f"Training with no of clusters = {idx}. . .")
    kmeans_train.fit(X)
    return kmeans_train.predict(X), kmeans_train.cluster_centers_
    
  

if __name__ == "__main__":
    labels, centers = train(X)
    plt.scatter(X[:, 0], X[:, 1], c = labels)
    plt.scatter(centers[:, 0], centers[:, 1], s=200, c='black', marker='X', label='Centroids')
    plt.show()
