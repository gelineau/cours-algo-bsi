from __future__ import annotations
import random
import time

from matplotlib import pyplot as plt
from my_dictionary import (
    Dictionary,
    create_empty_dictionary,
    insert_into_dictionary,
    get_value,
)


def initialize_dictionary(size: int, elements_created: int) -> Dictionary:
    dictionary = create_empty_dictionary(size)
    for i in range(elements_created):
        insert_into_dictionary(f"key {i}", i, dictionary)
    return dictionary


# sizes to test
sizes = [
    1000,
    20_000,
    30_000,
    50_000,
    60_000,
    80_000,
    100_000,
    150_000,
    200_000,
    250_000,
    300_000,
]


number_of_tries_dictionary_lookup = 20_000
number_of_tries_dictionary_lookup2 = 20_000


mean_times_dictionary_lookup = []
mean_times_dictionary_lookup1 = []
mean_times_dictionary_lookup2 = []


for size in sizes:
    print(f"{size=}")
    dictionary = initialize_dictionary(5000, size)
    dictionary1 = initialize_dictionary(50_000, size)
    dictionary2 = initialize_dictionary(5_000_000, size)
    start_time = time.time()
    for try_number in range(number_of_tries_dictionary_lookup):
        choice = random.randrange(size)
        get_value(f"key {choice}", dictionary)
    duration = time.time() - start_time
    mean_times_dictionary_lookup.append(duration)

    start_time = time.time()
    for try_number in range(number_of_tries_dictionary_lookup):
        choice = random.randrange(size)
        get_value(f"key {choice}", dictionary1)
    duration = time.time() - start_time
    mean_times_dictionary_lookup1.append(duration)

    start_time = time.time()
    for try_number in range(number_of_tries_dictionary_lookup2):
        choice = random.randrange(size)
        get_value(f"key {choice}", dictionary2)
    duration = time.time() - start_time
    mean_times_dictionary_lookup2.append(duration)


# Plot the results
plt.plot(sizes, mean_times_dictionary_lookup)
plt.plot(sizes, mean_times_dictionary_lookup1)
plt.plot(sizes, mean_times_dictionary_lookup2)

plt.xlabel("Size")
plt.ylabel("Time Taken (seconds)")
plt.show()
