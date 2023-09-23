import numpy as np

import random
from realtime_kmeans.rt_kmeans import RealTimeKMeans
import time

if __name__ == "__main__":
    num_points = 10_000_000

    data_points = [random.randint(0, 1000) for _ in range(num_points)]

    # Create histograms
    bin_edges = np.linspace(0, 1000, 100)  # 100 bins
    real_time_kmeans = RealTimeKMeans(bin_edges, k=3)

    batch_size = 100_000

    for i in range(0, num_points, batch_size):
        real_time_kmeans.update([data_points[i:i + batch_size]])

    start_time = time.time()
    labels, centroids = real_time_kmeans.cluster()

    end_time = time.time()

    print("Labels:", labels)
    print("Centroids:", centroids)
    print(f"Time taken to cluster 100 million data points: {end_time - start_time:.2f} seconds")
