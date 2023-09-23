import numpy as np
from realtime_kmeans.realtime_histogram import RealTimeHistogram
import random

def test_rt_hist():
    # Example usage:
    bin_edges = np.linspace(0, 100, 11)
    histogram = RealTimeHistogram(bin_edges=bin_edges)

    # Simulate real-time data update
    for _ in range(10):
        new_data = [random.randint(0, 100) for _ in range(10)]
        histogram.update(new_data)

    assert histogram is not None