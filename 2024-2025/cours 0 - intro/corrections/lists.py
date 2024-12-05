from __future__ import annotations


def search_number(numbers: list[int], number_to_find: int) -> bool:
    """
    Find if a value is present in a list of integers
    Complexity: O(n)
    """
    for number in numbers:
        if number == number_to_find:
            return True

    return False


def search_position(numbers: list[int], number_to_find: int) -> int | None:
    """
    Find at which position a value is present in a list of integers
    Complexity: O(n)
    """
    for index in range(len(numbers)):
        number = numbers[index]
        if number == number_to_find:
            return index
    return None


def calculate_mean(numbers: list[int]) -> float:
    """
    Calculate the mean of a list of integers
    Complexity: O(n)
    """
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)


def calculate_max(numbers: list[int]) -> int:
    """
    Calculate the maximum of a list of integers
    Complexity: O(n)
    """
    max = numbers[0]  # if list is empty, it will raise an exception
    for number in numbers[1:]:
        if number > max:
            max = number
    return max


def calculate_sum(numbers: list[int]) -> int:
    """
    Calculate the sum of a list of integers
    Complexity: O(n)
    """
    sum = 0
    for number in numbers:
        sum += number
    return sum


def replace_zero_by_rolling_sum(my_numbers: list[int]):
    """
    Replace each zero by the sum of all integers before it
    Version 1:
    Complexity: O(n^2)
    """
    for index in range(len(my_numbers)):
        if my_numbers[index] == 0:
            rolling_sum = calculate_sum(my_numbers[:index])
            my_numbers[index] = rolling_sum


def replace_zero_by_rolling_sum2(my_numbers: list[int]):
    """
    Replace each zero by the sum of all integers before it
    Version 2:
    Complexity: O(n)
    """
    rolling_sum = 0
    for index in range(len(my_numbers)):
        if my_numbers[index] == 0:
            my_numbers[index] = rolling_sum
        rolling_sum += my_numbers[index]


my_numbers = [1, 2, 0, 8, 4, 0]

print(
    f"""
{search_number(my_numbers, 2)=}
{search_number(my_numbers, 12)=}
{search_position(my_numbers, 8)=}
{calculate_mean(my_numbers)=}
{calculate_max(my_numbers)=}
"""
)

replace_zero_by_rolling_sum(my_numbers)
print(my_numbers)

my_numbers = [1, 2, 0, 8, 4, 0]
replace_zero_by_rolling_sum2(my_numbers)
print(my_numbers)
