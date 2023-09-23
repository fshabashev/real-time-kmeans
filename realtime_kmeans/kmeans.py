import numpy as np


def weighted_kmeans_1d(data, weights, k, max_iters=100, tol=1e-4):
    # Initialize centroids by randomly selecting k data points
    centroids = data[np.random.choice(len(data), k, replace=False)]

    for _ in range(max_iters):
        # Assignment step: Assign each data point to the nearest centroid
        distances = np.abs(data[:, np.newaxis] - centroids)
        labels = np.argmin(distances, axis=1)

        # Update step: Recompute centroids based on weighted mean
        new_centroids = np.array(
            [np.average(data[labels == i], weights=weights[labels == i]) for i in range(k)])

        # Check for convergence
        if np.all(np.abs(new_centroids - centroids) < tol):
            break

        centroids = new_centroids

    return labels, centroids
