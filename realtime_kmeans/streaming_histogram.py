from collections import deque


class StreamingHistogram:
    def __init__(self, data_range=(0, 100000), num_bins=100000, max_data_points=1400):
        self.data_range = data_range
        self.num_bins = num_bins
        self.bin_width = (data_range[1] - data_range[0]) / num_bins
        self.histogram = [0] * num_bins
        self.queue = deque(maxlen=max_data_points)
        self.max_data_points = max_data_points

    def update(self, data_point):
        if self.max_data_points and len(self.queue) == self.max_data_points:
            old_data_point = self.queue.popleft()
            old_bin_index = int(old_data_point / self.bin_width)
            self.histogram[old_bin_index] -= 1

        self.queue.append(data_point)
        bin_index = int(data_point / self.bin_width)
        self.histogram[bin_index] += 1

    def batch_update(self, data_points):
        for data_point in data_points:
            self.update(data_point)

    def get_histogram(self):
        return self.histogram
