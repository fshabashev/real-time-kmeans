import numpy as np


class RealTimeHistogram:
    def __init__(self, bin_edges):
        self.bin_edges = bin_edges
        self.bin_counts = np.zeros(len(bin_edges) - 1)

    def update(self, new_data):
        # Update histogram counts with new data
        counts, _ = np.histogram(new_data, bins=self.bin_edges)
        self.bin_counts += counts

    def get_density(self):
        total_data_points = sum(self.bin_counts)
        densities = [count / total_data_points for count in self.bin_counts]
        return densities

    def get_histogram(self):
        return self.bin_edges, self.bin_counts


