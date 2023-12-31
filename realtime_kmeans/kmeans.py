import numpy as np


def weighted_kmeans_1d(data, weights, k, max_iters=100, tol=1e-4):
    if not isinstance(data, np.ndarray):
        raise ValueError("data must be a numpy array")
    if not isinstance(weights, np.ndarray):
        raise ValueError("weights must be a numpy array")
    if data.ndim != 1:
        raise ValueError("data must be a one-dimensional numpy array")
    if weights.ndim != 1:
        raise ValueError("weights must be a one-dimensional numpy array")
    if data.shape != weights.shape:
        raise ValueError("data and weights must have the same shape")
    if np.any(weights < 0):
        raise ValueError("weights cannot be negative")

    # Filter out data points with zero weights
    nonzero_indices = np.where(weights > 0)[0]
    data = data[nonzero_indices]
    weights = weights[nonzero_indices]

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
