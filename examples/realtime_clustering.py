# Import necessary modules
from realtime_kmeans.streaming_histogram import StreamingHistogram
from realtime_kmeans.rt_kmeans import RealTimeKMeans


if __name__ == "__main__":
    # Initialize parameters
    import numpy as np
    from realtime_kmeans.kmeans import weighted_kmeans_1d
    from realtime_kmeans.streaming_histogram import StreamingHistogram

    # ... [RealTimeKMeans class here] ...

    # Parameters for RealTimeKMeans
    data_range = (0, 100000)
    num_bins = 100000
    k = 5
    max_data_points = 1400
    max_iters = 100
    tol = 1e-4

    # Create an instance of RealTimeKMeans
    rt_kmeans = RealTimeKMeans(data_range, num_bins, k, max_data_points, max_iters, tol)

    # Generate a massive stream of data
    data_size = 10 ** 6
    data_stream = np.random.uniform(0, 100000, data_size)  # Random data points between 0 and 100000

    # Update the histogram with the streaming data in chunks
    chunk_size = 1000
    for i in range(0, data_size, chunk_size):
        rt_kmeans.update(data_stream[i:i + chunk_size])

    # Perform clustering
    labels, centroids = rt_kmeans.cluster()

    # Print results
    print("Centroids:", centroids)
