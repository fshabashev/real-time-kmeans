from realtime_kmeans.streaming_histogram import StreamingHistogram
import random


def data_stream(data_range=(0, 100000)):
    while True:
        yield random.randint(data_range[0], data_range[1])


if __name__ == "__main__":
    # Usage:
    streaming_histogram = StreamingHistogram()

    # Simulating the stream
    stream = data_stream()

    # Process 5000 data points from the stream for demonstration
    for _ in range(5000):
        data_point = next(stream)
        streaming_histogram.update(data_point)

    # To get the current histogram
    current_histogram = streaming_histogram.get_histogram()
    print(current_histogram)
