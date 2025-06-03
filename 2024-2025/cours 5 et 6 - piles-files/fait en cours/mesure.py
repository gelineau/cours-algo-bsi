import time

repetitions = 10

times = []
queue_sizes = [
    1,
    10,
    100,
    1000,
    10_000,
    100_000,
    1_000_000,
    2_000_000,
    4_000_000,
    6_000_000,
    8_000_000,
    10_000_000,
]


def calculate_time(size: int) -> float:
    my_list = []
    for _ in range(size):
        my_list.append(0)

    time_before = time.time()
    for _ in range(10):
        my_list.insert(0, 0)

    time_after = time.time()
    return time_after - time_before


for size in queue_sizes:
    elapsed_time = calculate_time(size)
    print(f"{size}\t{elapsed_time}")
