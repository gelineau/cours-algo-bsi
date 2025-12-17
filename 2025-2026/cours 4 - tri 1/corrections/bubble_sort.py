from __future__ import annotations

import random


def swap(data: list[int], index1: int, index2: int):
    data[index1], data[index2] = data[index2], data[index1]


def bubble_sort(data: list[int]):
    for step in range(len(data)):  # len(data) - 1
        for index_to_sort in range(len(data) - 1):  # len(data) - step - 1
            if data[index_to_sort] > data[index_to_sort + 1]:
                swap(data, index_to_sort, index_to_sort + 1)


random.seed(42)

for function in (bubble_sort, bubble_sort2, bubble_sort3):
    for _ in range(100):
        input = [random.randrange(15) for _ in range(15)]
        function(input)
        assert input == sorted(input), f"{input=} {sorted(input)=}"
    print("OK")
