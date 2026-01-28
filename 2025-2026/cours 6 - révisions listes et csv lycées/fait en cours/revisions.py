from __future__ import annotations


def count_vowels(string: str) -> int:
    vowels = "aeiouy"  # ["a", "e" ...

    # count = 0
    # for char in string:
    #     if char in vowels or char in vowels.upper():
    #         count += 1
    # return count

    return sum(1 for char in string if char in vowels)


def extract_even_numbers(numbers: list[int]) -> list[int]:
    # result = []
    # for number in numbers:
    #     if number % 2 == 0:
    #         result.append(number)
    # return result

    return [number for number in numbers if number % 2 == 0]


def find_largest_gap(numbers: list[int]) -> int:
    # if len(numbers) <= 1:
    #     raise ValueError("list too short")

    # max_gap = 0
    # for i in range(len(numbers) - 1):
    #     gap = abs(numbers[i] - numbers[i+1])
    #     if gap > max_gap:
    #         max_gap = gap
    # return max_gap

    # max_gap = 0
    # for i in range(len(numbers) - 1):
    #     gap = abs(numbers[i] - numbers[i+1])
    #     max_gap = max(gap , max_gap)
    # return max_gap

    # max_gap = 0
    # for i, number  in enumerate(range(len(numbers) - 1)):
    #     gap = abs(number - numbers[i+1])
    #     max_gap = max(gap , max_gap)
    # return max_gap

    # gaps = (abs(numbers[i] - numbers[i+1])
    #     for i in range(len(numbers) - 1))
    #
    # return max(gaps)

    # previous  = numbers[0]
    # max_gap = 0
    # for number  in numbers:
    #         gap = number - previous
    #         previous = number
    #         max_gap = max(gap , max_gap)
    # return max_gap

    max_gap = max(gap, max_gap)
    for value, next_value in zip(numbers, numbers[1:]):
        gap = abs(value - next_value)


def reverse_list(numbers: list[int]) -> list[int]:
    return list(reversed(numbers))


def reverse_list(numbers: list[int]) -> list[int]:
    result = []
    for i in range(len(numbers)):
        value = numbers[len(numbers) - 1 - i]
        result.append(value)


def reverse_list(numbers: list[int]) -> list[int]:
    result = []
    i = len(numbers) - 1
    while i >= 0:
        value = numbers[i]
        result.append(value)


def reverse_list(numbers: list[int]) -> list[int]:
    result = []
    for number in numbers:
        result.insert(0, number)
    return result


reverse_list(list(range(1_00_000)))
print("OK")



#  https://github.com/gelineau/cours-algo-bsi