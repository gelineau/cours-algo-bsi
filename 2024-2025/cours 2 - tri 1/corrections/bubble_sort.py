from __future__ import annotations

import random


def swap(data: list[int], index1: int, index2: int):
    x = data[index1]
    data[index1] = data[index2]
    data[index2] = x


def bubble_sort2(data: list[int]):
    for step in range(len(data) - 1):
        for index_to_sort in range(0, len(data) - step - 1):
            if data[index_to_sort] > data[index_to_sort + 1]:
                swap(data, index_to_sort, index_to_sort + 1)


def bubble_sort(data: list[int]):
    for last in range(len(data) - 1, 0, -1):
        for index_to_sort in range(0, last):
            if data[index_to_sort] > data[index_to_sort + 1]:
                swap(data, index_to_sort, index_to_sort + 1)


random.seed(42)
for _ in range(100):
    input = [random.randrange(15) for _ in range(15)]
    bubble_sort(input)
    assert input == sorted(input), f"{input=} {sorted(input)=}"
print("OK")
