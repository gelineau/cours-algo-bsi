from __future__ import annotations

import random


def swap(data: list[int], index1: int, index2: int):
    x = data[index1]
    data[index1] = data[index2]
    data[index2] = x

    # other solution:
    # data[index1], data[index2] = data[index2], data[index1]


def partition(data: list[int], min_index: int, max_index: int) -> int:
    """
    Separate the data (from min_index to max_index) into 2 parts:
    first part contains "little" elements (less than pivot)
    second part contains "big" elements (more than pivot)
    second part should start with pivot

    return the index of second part (which contains pivot)
    """
    pivot = data[max_index]
    start_index_of_bigs = min_index

    for index_to_compare in range(min_index, max_index + 1):
        if data[index_to_compare] <= pivot:
            swap(data, index_to_compare, start_index_of_bigs)
            start_index_of_bigs += 1

    # on last iteration, pivot was swapped into start_index_of_bigs index,
    # but we made start_index_of_bigs += 1
    return start_index_of_bigs - 1


def quick_sort_on_part(data: list[int], min_index: int, max_index: int):
    pivot_index = partition(data, min_index, max_index)

    if pivot_index - 1 > min_index:
        quick_sort_on_part(data, min_index, pivot_index - 1)
    if pivot_index + 1 < max_index:
        quick_sort_on_part(data, pivot_index + 1, max_index)


def quick_sort(data: list[int]):
    quick_sort_on_part(data, 0, len(data) - 1)


random.seed(42)
for i in range(1, 100):
    input = [random.randrange(15) for _ in range(i)]
    quick_sort(input)
    assert input == sorted(input), f"{input=} {sorted(input)=}"
print("OK")
