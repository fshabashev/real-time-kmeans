class StreamingHistogram:
    def __init__(self, data_range=(0, 100000), num_bins=100000, max_data_points=1400):
        self.data_range = data_range
        self.num_bins = num_bins
        self.bin_width = (data_range[1] - data_range[0]) / num_bins
        self.histogram = [0] * num_bins
        self.queue = []
        self.max_data_points = max_data_points

    def update(self, data_point):
        # Add new data point to the queue
        self.queue.append(data_point)

        # Find the bin for the new data point and increment its count
        bin_index = int(data_point / self.bin_width)
        self.histogram[bin_index] += 1

        # If queue exceeds max_data_points, remove the oldest one
        if self.max_data_points and len(self.queue) > self.max_data_points:
            old_data_point = self.queue.pop(0)
            # Find the bin for the old data point and decrement its count
            old_bin_index = int(old_data_point / self.bin_width)
            self.histogram[old_bin_index] -= 1

    def get_histogram(self):
        return self.histogram
