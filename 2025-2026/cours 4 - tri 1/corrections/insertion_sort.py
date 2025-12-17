from __future__ import annotations

import random


def insertion_sort(data: list[int]):
    for index_to_sort in range(1, len(data)):  # n - 1 fois
        value_to_sort = data[index_to_sort]
        index_to_move = index_to_sort - 1
        while index_to_move >= 0 and data[index_to_move] > value_to_sort:
            data[index_to_move + 1] = data[index_to_move]
            index_to_move -= 1
        data[index_to_move + 1] = value_to_sort


# def insertion_sort2(data: list[int]):
#     for index_to_sort in range(1, len(data)):
#         value_to_sort = data[index_to_sort]
#         for index_to_compare in range(index_to_sort - 1, -1, -1):
#             if data[index_to_compare] <= value_to_sort:
#                 break
#             data[index_to_compare + 1] = data[index_to_compare]
#
#         data[index_to_compare] = value_to_sort


random.seed(42)
for _ in range(100):
    input = [random.randrange(15) for _ in range(15)]
    insertion_sort(input)
    assert input == sorted(input), f"{input=} {sorted(input)=}"
print("OK")
