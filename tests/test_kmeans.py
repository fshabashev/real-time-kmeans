import random

import numpy as np
from sklearn.cluster import KMeans
from realtime_kmeans.rt_kmeans import RealTimeKMeans


def generate_clustered_data(num_clusters, points_per_cluster, cluster_spread=5000, data_range=(0, 99_000)):
    centers = np.linspace(data_range[0] + 10000, data_range[1] - 10000, num_clusters)
    data = []

    for center in centers:
        data.extend(np.random.normal(center, cluster_spread, points_per_cluster))

    # Clip data to ensure it's within the specified range
    return np.clip(data, data_range[0], data_range[1]), centers


def test_kmeans_similarity():
    # Generate random data
    np.random.seed(42)

    # Generate clustered data
    data, centers = generate_clustered_data(num_clusters=5, points_per_cluster=2000)
    k = 5

    # Normal KMeans clustering
    kmeans = KMeans(n_clusters=k, random_state=0).fit(data.reshape(-1, 1))
    normal_centroids = sorted(kmeans.cluster_centers_.ravel())

    # Histogram-based KMeans clustering
    rt_kmeans = RealTimeKMeans(data_range=(0, 100000), num_bins=100000, k=k)
    rt_kmeans.update(data)
    _, histogram_centroids = rt_kmeans.cluster()
    histogram_centroids = sorted(histogram_centroids)

    # Compare centroids
    diff = np.abs(np.array(normal_centroids) - np.array(histogram_centroids))
    assert np.all(diff < 10), f"Centroids differ by more than tolerance: {diff}"
