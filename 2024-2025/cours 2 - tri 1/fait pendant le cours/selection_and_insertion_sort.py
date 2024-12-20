import time
import random


def find_index_of_min(numbers: list[int], start_index: int) -> int:
    min_value = numbers[start_index]
    min_index = start_index
    for index_to_search in range(start_index, len(numbers)):
        if numbers[index_to_search] < min_value:
            min_index = index_to_search
            min_value = numbers[index_to_search]
    return min_index


def swap(numbers: list[int], index1: int, index2: int):
    # tmp = numbers[index1]
    # numbers[index1] = numbers[index2]
    # numbers[index2] = tmp

    numbers[index1], numbers[index2] = numbers[index2], numbers[index1]


def sort_by_selection(numbers: list[int]):
    for index in range(0, len(numbers) - 1):
        min_index = find_index_of_min(numbers, index)
        swap(numbers, index, min_index)


# print(f"{find_index_of_min([1,6,9,4, 1, 8], 1)}")
# find_index_of_min([12], 0)
#


def sort_by_insertion(numbers: list[int]):
    for index_to_sort in range(1, len(numbers)):
        value_to_sort = numbers[index_to_sort]
        index_to_move = index_to_sort - 1
        while index_to_move >= 0 and numbers[index_to_move] > value_to_sort:
            numbers[index_to_move + 1] = numbers[index_to_move]
            index_to_move -= 1
        numbers[index_to_move + 1] = value_to_sort


numbers = [9, 6, 1, 4, 8]


# n = 10000000
# numbers = [random.randrange(100) for _ in range(n)]
# start = time.time()
# # sort_by_insertion(numbers)
# numbers.sort()
# end = time.time()
#
# print(end - start)
#
#
# n = 20000000
# numbers = [random.randrange(100) for _ in range(n)]
# start = time.time()
# # sort_by_insertion(numbers)
# numbers.sort()
# end = time.time()
#
# print(end - start)


def bubble_sort(data: list[int]):
    for last in range(len(data) - 1, 0, -1):
        for index_to_sort in range(0, last):
            if data[index_to_sort] > data[index_to_sort + 1]:
                swap(data, index_to_sort, index_to_sort + 1)


# def bubble_sort(data: list[int]):
#     for last in range(len(data)-1, 0, -1):
#         if data[index_to_sort] > data[index_to_sort + 1]:
#             swap(data, index_to_sort, index_to_sort + 1)
#     for index_to_sort in range(0, last):
#             if data[index_to_sort] > data[index_to_sort + 1]:
#                 sw²ap(data, index_to_sort, index_to_sort + 1)


for i in range(10):
    for j in range(10):
        print(i)
