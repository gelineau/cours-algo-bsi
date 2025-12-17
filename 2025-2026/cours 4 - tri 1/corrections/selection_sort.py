from __future__ import annotations

import random


def swap(data: list[int], index1: int, index2: int):
    data[index1], data[index2] = data[index2], data[index1]


def selection_sort(data: list[int]):
    for index_to_sort in range(0, len(data) - 1):
        index_minimum = find_index_of_minimum(data, index_to_sort)
        swap(data, index_minimum, index_to_sort)


def find_index_of_minimum(data: list[int], start_index: int) -> int:
    value_minimum = data[start_index]
    index_minimum = start_index
    for index_to_compare in range(start_index + 1, len(data)):
        if data[index_to_compare] < value_minimum:
            value_minimum = data[index_to_compare]
            index_minimum = index_to_compare
    return index_minimum


random.seed(42)
for _ in range(100):
    input = [random.randrange(15) for _ in range(15)]
    selection_sort(input)
    assert input == sorted(input), f"{input=} {sorted(input)=}"
print("OK")
