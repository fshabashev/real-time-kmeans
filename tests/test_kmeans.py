from realtime_kmeans.kmeans import weighted_kmeans
import numpy as np


def test_happypath():
    # Example usage:
    data = np.array([
        [1, 2],
        [5, 6],
        [1, 1],
        [5, 5],
        [2, 2],
        [6, 6]
    ])
    weights = np.array([1, 2, 1, 2, 1, 2])
    k = 2

    labels, centroids = weighted_kmeans(data, weights, k)
    assert labels is not None