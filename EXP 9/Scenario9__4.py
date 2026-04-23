print("SY-5", "Raj Ghule", "Roll_no-40")

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X = np.array([
    [1, 2], [2, 3], [3, 4],
    [8, 7], [9, 8], [10, 9]
])

best_k = 0
best_score = -1

for k in range(2, 5):
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(X)

    score = silhouette_score(X, labels)
    print(f"k = {k}, Silhouette Score = {score}")

    if score > best_score:
        best_score = score
        best_k = k

print("\nOptimal number of clusters (k):", best_k)