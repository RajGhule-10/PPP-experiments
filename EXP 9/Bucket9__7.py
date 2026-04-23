print("SY-5", "Raj Ghule", "Roll_no-40")

import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X = np.array([
    [1, 2], [2, 3], [3, 4],
    [8, 7], [9, 8], [10, 9]
])

kmeans = KMeans(n_clusters=2, random_state=42)
labels = kmeans.fit_predict(X)

score = silhouette_score(X, labels)

print("Silhouette Score:", score)