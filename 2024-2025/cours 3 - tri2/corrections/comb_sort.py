from __future__ import annotations

import random


def swap(data: list[int], index1: int, index2: int):
    x = data[index1]
    data[index1] = data[index2]
    data[index2] = x


def comb_sort(data: list[int]):
    interval = len(data)
    is_swapped = False
    while interval > 1 or is_swapped:
        interval = max(1, int(interval / 1.3))
        is_swapped = False
        print(f"{interval=} {data=}")
        for index_to_sort in range(len(data) - interval):
            if data[index_to_sort] > data[index_to_sort + interval]:
                swap(data, index_to_sort, index_to_sort + interval)
                is_swapped = True


random.seed(42)
for _ in range(100):
    print(f"{_=}")
    input = [random.randrange(15) for _ in range(15)]
    comb_sort(input)
    assert input == sorted(input), f"{input=} {sorted(input)=}"
print("OK")
