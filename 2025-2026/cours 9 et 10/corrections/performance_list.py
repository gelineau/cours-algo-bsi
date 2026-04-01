import time
import random

from matplotlib import pyplot as plt
from my_dictionary_oop import Dictionary


def measure_list_append_pop_left(numbers_size: int, repetitions: int) -> float:
    # Create and initialize a list
    numbers = [random.randrange(100000) for _ in range(numbers_size)]

    start_time = time.time()
    for _ in range(repetitions):
        numbers.append(numbers_size)
        numbers.pop(0)
    total_time = time.time() - start_time

    return total_time / repetitions


def measure_list_append_pop_right(numbers_size: int, repetitions: int) -> float:
    # Create and initialize a list
    numbers = [random.randrange(100000) for _ in range(numbers_size)]

    start_time = time.time()
    for _ in range(repetitions):
        numbers.append(numbers_size)
        numbers.pop()
    total_time = time.time() - start_time

    return total_time / repetitions


def measure_list_access(numbers_size: int, repetitions: int) -> float:
    # Create and initialize a list
    numbers = [random.randrange(100000) for _ in range(numbers_size)]

    start_time = time.time()
    for _ in range(repetitions):
        a = numbers[numbers_size // 3]
    total_time = time.time() - start_time

    return total_time / repetitions


def measure_list_sort(numbers_size: int, repetitions: int) -> float:
    # Create and initialize a list
    numbers = [random.randrange(100000) for _ in range(numbers_size)]

    start_time = time.time()
    for _ in range(repetitions):
        numbers.sort()
        numbers.sort(reverse=True)
    total_time = time.time() - start_time

    return total_time / repetitions


def measure_dict_access(
    numbers_size: int, repetitions: int, dictionary_size: int
) -> float:
    # Create and initialize a Dictionary
    dictionary = Dictionary(size=dictionary_size)
    for i in range(numbers_size):
        dictionary[f"key {i}"] = random.randrange(100000)

    start_time = time.time()
    for i in range(repetitions):
        a = dictionary[f"key {numbers_size-1}"]
    total_time = time.time() - start_time

    return total_time / repetitions


def plot():
    times = []
    sizes = [1000, 5_000, 10_000, 20_000, 30_000]

    for size in sizes:
        # total_time = measure_list_append_pop_left(size, repetitions=100_000)
        total_time = measure_list_append_pop_right(size, 1000_000)
        # total_time = measure_list_access(size, 1_000_000)
        # total_time = measure_list_sort(size, 100)
        # total_time = measure_list_sort(size, 100)
        # total_time = measure_dict_access(size, 100_000, dictionary_size=100_000)
        # total_time = measure_dict_access(size, 100_000, dictionary_size=1_000)
        print(f"Time: {total_time} seconds")
        times.append(total_time)

    # Plotting the results
    plt.figure(figsize=(12, 6))

    plt.plot(sizes, times)
    plt.ylim(bottom=0)
    plt.xlabel("Size")
    plt.ylabel("Time (seconds)")
    plt.grid(True)
    plt.show()


plot()
