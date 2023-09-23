from realtime_kmeans.kmeans import weighted_kmeans_1d
from realtime_kmeans.realtime_histogram import RealTimeHistogram


class RealTimeKMeans:
    def __init__(self, bin_edges, k, max_iters=100, tol=1e-4):
        self.histogram = None
        self.k = k
        self.max_iters = max_iters
        self.tol = tol
        self.bin_edges = bin_edges

    def update(self, new_data_list):
        # Update histograms with new data
        if self.histogram is None:
            self.histogram = RealTimeHistogram(self.bin_edges)
        self.histogram.update(new_data_list)

    def cluster(self):
        # Convert histograms to vectors (using bin counts)
        weights = self.histogram.bin_counts

        coordinates = (self.histogram.bin_edges[:-1] + self.histogram.bin_edges[1:])/2

        labels, centroids = weighted_kmeans_1d(coordinates, weights, self.k, self.max_iters, self.tol)
        return labels, centroids

