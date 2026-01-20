from __future__ import annotations

import random


def swap(data: list[int], index1: int, index2: int):
    data[index1], data[index2] = data[index2], data[index1]


def partition(data: list[int], min_index: int, max_index: int) -> int:
    """
    Separate the data (from min_index to max_index) into 2 parts:
    first part contains "little" elements (less than pivot)
    second part contains "big" elements (more than pivot)
    second part should start with pivot

    return the index of second part (which contains pivot)
    """
    pivot = data[max_index]
    print(f"{pivot=}")
    print(f"{data=}")
    start_index_of_bigs = min_index

    for index_to_compare in range(min_index, max_index + 1):
        print(f"{index_to_compare=}")
        if data[index_to_compare] <= pivot:
            print(f"swap {data[index_to_compare]} {data[start_index_of_bigs]}")
            swap(data, index_to_compare, start_index_of_bigs)
            print(data)
            start_index_of_bigs += 1

    # on last iteration, pivot was swapped into start_index_of_bigs index,
    # but we made start_index_of_bigs += 1
    return start_index_of_bigs - 1


def quick_sort_on_part(data: list[int], min_index: int, max_index: int):
    if max_index <= min_index:
        return

    pivot_index = partition(data, min_index, max_index)
    quick_sort_on_part(data, min_index, pivot_index - 1)
    quick_sort_on_part(data, pivot_index + 1, max_index)


def quick_sort(data: list[int]):
    if data != []:
        quick_sort_on_part(data, 0, len(data) - 1)


quick_sort([8, 4, 1, 15, 7, 16, 12, 7])


# pivot=7
# data=[8, 4, 1, 15, 7, 16, 12, 7]
# index_to_compare=0
# index_to_compare=1
# swap 4 8
# [4, 8, 1, 15, 7, 16, 12, 7]
# index_to_compare=2
# swap 1 8
# [4, 1, 8, 15, 7, 16, 12, 7]
# index_to_compare=3
# index_to_compare=4
# swap 7 8
# [4, 1, 7, 15, 8, 16, 12, 7]
# index_to_compare=5
# index_to_compare=6
# index_to_compare=7
# swap 7 15
# [4, 1, 7, 7, 8, 16, 12, 15]


# random.seed(42)
# for i in range(1, 100):
#     input = [random.randrange(15) for _ in range(i)]
#     quick_sort(input)
#     assert input == sorted(input), f"{input=} {sorted(input)=}"
#
# input = [random.randrange(15)]
# quick_sort(input)
# assert input == sorted(input), f"{input=} {sorted(input)=}"
#
# input = []
# quick_sort(input)
# assert input == sorted(input), f"{input=} {sorted(input)=}"
#
# print("OK")
