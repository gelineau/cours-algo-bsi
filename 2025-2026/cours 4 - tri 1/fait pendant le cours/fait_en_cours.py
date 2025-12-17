from __future__ import annotations


def double_list(numbers: list[int]) -> list[int]:
    """O(n)"""
    new_list = []
    for number in numbers:
        new_list.append(2 * number)
    return new_list


def add_42(numbers: list[int]):
    numbers.append(42)


def swap(numbers: list[int], i1: int, i2: int):
    # tmp = numbers[i1]
    # numbers[i1] = numbers[i2]
    # numbers[i2] = tmp
    numbers[i1], numbers[i2] = numbers[i2], numbers[i1]


def bubble_sort(numbers: list[int]) -> None:
    for step in range(len(numbers) - 1):
        for i in range(len(numbers) - 1 - step):
            if numbers[i] > numbers[i + 1]:
                swap(numbers, i, i + 1)


numbers = [8, 1, 9, 6, 4]
bubble_sort(numbers)
print(numbers)


def get_minimum_indice(numbers: list[int], i_begin: int) -> int:
    """O(n)"""
    i_min = i_begin
    min_number = numbers[i_min]
    for i in range(i_begin, len(numbers)):
        if numbers[i] < min_number:
            i_min = i
            min_number = numbers[i]
    return i_min


def selection_sort(numbers: list[int]):
    for i in range(len(numbers) - 1):
        i_min = get_minimum_indice(numbers, i)
        swap(numbers, i, i_min)


numbers = [8, 1, 9, 6, 4]
selection_sort(numbers)
print(numbers)


def insertion_sort(numbers: list[int]) -> None:
    for i in range(len(numbers) - 1):
        indice_to_move = i + 1
        while (
            indice_to_move > 0 and numbers[indice_to_move] < numbers[indice_to_move - 1]
        ):
            swap(numbers, indice_to_move, indice_to_move - 1)
            print(numbers)
            indice_to_move -= 1


numbers = [8, 1, 9, 6, 4]
insertion_sort(numbers)
print(numbers)
