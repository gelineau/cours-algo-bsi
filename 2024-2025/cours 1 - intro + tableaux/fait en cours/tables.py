# from __future__ import annotations
# ... if old python version


def find(value: int, numbers: list[int]) -> bool:
    for number in numbers:
        if number == value:
            return True
    return False


def find_position(number_to_find: int, numbers: list[int]) -> int | None:
    for index in range(len(numbers)):
        value = numbers[index]
        if value == number_to_find:
            return index
    return None

def calculate_mean(numbers: list[int])-> float:
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)

def insert(number: int, index_insertion: int, numbers: list[int]):
    numbers.append(None)

    index_copy = len(numbers) - 1
    while index_copy >= index_insertion + 1:
        numbers[index_copy] = numbers[index_copy -1]
        index_copy -= 1

    numbers[index_insertion] = number

def calculate_sum(numbers: list[int]) -> int:
    # complexity O(n)
    sum = 0
    for number in numbers:
        sum += number
    return sum

def replace_0_by_rolling_sum(numbers: list[int]):
    for index in range(len(numbers)):
        if numbers[index] == 0:
            sum = 0
            for j in range(index):
                sum += numbers[j]
            numbers[index] = sum

def replace_0_by_rolling_sum_on(numbers: list[int]):
    rolling_sum = 0
    for index in range(len(numbers)):
        if numbers[index] == 0:
            numbers[index] = rolling_sum
        rolling_sum += numbers[index]



numbers = [2, 4, 3, 3]

print(f"{find(3, numbers)=} {find(42, numbers)=}")
