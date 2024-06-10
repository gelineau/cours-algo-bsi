from __future__ import annotations
import random
import time

from matplotlib import pyplot as plt


def initialize_list(elements_number: int) -> list[str]:
    result = []
    for i in range(elements_number):
        result.append(f"value {i}")
    return result


# sizes to test
elements_numbers = [1000, 5000, 10000, 20000, 30000, 50000, 60000, 80000, 100000]


number_of_tries_list_lookup = 1_000_000
number_of_tries_list_append = 1_000_000
number_of_tries_list_insertion = 40_000
number_of_tries_product = 1

mean_times_list_lookup = []
mean_times_list_insertion = []
mean_times_product = []
mean_times_list_append = []

for element_number in elements_numbers:
    print(f"{element_number=}")
    my_list = initialize_list(element_number)
    start_time = time.time()
    for try_number in range(number_of_tries_list_lookup):
        choice = random.randrange(element_number)
        a = my_list[choice]
    duration = time.time() - start_time
    mean_times_list_insertion.append(duration)

    start_time = time.time()
    for try_number in range(number_of_tries_list_insertion):
        choice = random.randrange(element_number)
        my_list.insert(choice, "insert")
        my_list.pop(choice)

    duration = time.time() - start_time

    mean_times_list_lookup.append(duration)

    start_time = time.time()
    for try_number in range(number_of_tries_product):
        for word1 in my_list[::30]:
            for word2 in my_list[::30]:
                a = word1 + word2
    duration = time.time() - start_time

    mean_times_product.append(duration)

    start_time = time.time()
    for try_number in range(number_of_tries_list_append):
        my_list.append("append")
        my_list.pop()
    duration = time.time() - start_time

    mean_times_list_append.append(duration)

# Plot the results
plt.plot(elements_numbers, mean_times_list_insertion)
plt.plot(elements_numbers, mean_times_list_lookup)
plt.plot(elements_numbers, mean_times_product)
plt.plot(elements_numbers, mean_times_list_append)
plt.xlabel("Element number")
plt.ylabel("Time Taken (seconds)")
plt.show()
