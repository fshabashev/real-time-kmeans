from realtime_kmeans.kmeans import weighted_kmeans_1d
from realtime_kmeans.streaming_histogram import StreamingHistogram
import numpy as np


class RealTimeKMeans:
    def __init__(self, data_range, num_bins, k, max_data_points=None, max_iters=100, tol=1e-4):
        self.histogram = StreamingHistogram(data_range=data_range, num_bins=num_bins, max_data_points=max_data_points)
        self.k = k
        self.max_iters = max_iters
        self.tol = tol

    def update(self, new_data_list):
        # Update histograms with new data
        self.histogram.batch_update(new_data_list)

    def cluster(self):
        # Convert histograms to vectors (using bin counts)
        weights = np.array(self.histogram.get_histogram())

        bin_width = (self.histogram.data_range[1] - self.histogram.data_range[0]) / self.histogram.num_bins
        coordinates = np.array([(i + 0.5) * bin_width for i in range(self.histogram.num_bins)])

        labels, centroids = weighted_kmeans_1d(coordinates, weights, self.k, self.max_iters, self.tol)
        return labels, centroids
