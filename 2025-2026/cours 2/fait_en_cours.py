from __future__ import annotations


# https://github.com/gelineau/cours-algo-bsi
#


## Exo 1

#
# def detail_words(sentence: str) -> None:
#     words = sentence.split()
#     # for index, word in enumerate(words):
#     #     print(f"{index+1}: {word} ({len (word)})")
#     for index in range(len(words)):
#         word = words[index]
#         print(f"{index+1}: {word} ({len (word)})")
#
#
# sentence = "oh temps suspends ton vol"
# detail_words(sentence)
#
#
# def double_list(numbers: list[int]) -> list[int]:
#     new_list = []
#
#     for number in numbers:
#         new_list.append(number * 2)
#
#     return new_list
#
#
# def double_list(numbers: list[int]) -> list[int]:
#     new_list = [number * 2 for number in numbers]
#
#     return new_list
#
#
# my_list = [1, 4, 3]
# new_list = double_list(my_list)
# print(new_list)


def calculate_lengths(names: list[str]) -> list[int]:
    lengths = []
    for name in names:
        if name.startswith("A"):
            length = len(name)
            lengths.append(length)
    return lengths


def calculate_lengths(names: list[str]) -> list[int]:
    # lengths = []
    # for name in names:
    #     if name.startswith("A"):
    #         length = len(name)
    #         lengths.append(length)
    lengths = [len(name) for name in names if name.startswith("A")]
    return lengths


first_names = ["Alice", "Bob", "Anna", "Charlie", "Amélie"]

print(calculate_lengths(first_names))


def search_number(number_to_find: int, numbers: list[int]) -> bool:
    # return number_to_find in numbers

    # for number in numbers:
    #     if number == number_to_find:
    #         return True
    # return False

    return any(number == number_to_find for number in numbers)


def search_position(numbers: list[int], number_to_find: int) -> int | None:
    for index in range(len(numbers)):
        number = numbers[index]
        if number == number_to_find:
            return index
    return None


def search_position(numbers: list[int], number_to_find: int) -> int | None:
    # for index, number in enumerate(numbers):
    #     if number == number_to_find:
    #         return index
    # return None
    try:
        return numbers.index(number_to_find)
    except ValueError:
        return None


def calculate_mean(numbers: list[int]) -> float:
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)


def calculate_mean(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers)


numbers = [2, 3, 5, 7]
# print(sum(number ** 2 for number in numbers))


print(calculate_mean([]))


def insert_element(numbers: list[int], value: int, position: int):
    numbers.insert(position, value)


def insert_element(numbers: list[int], value: int, position: int) -> list[int]:
    return numbers[:position] + [value] + numbers[position:]


def insert_element(numbers: list[int], value: int, position: int) -> list[int]:
    new_list = []
    # for i in range(len(numbers))
    for i, number in enumerate(numbers):
        if i == position:
            new_list.append(value)

        new_list.append(number)

    return new_list


def insert_element(numbers: list[int], value: int, position: int):
    numbers.append(None)
    for index in range(len(numbers) - 1, position - 1, -1):
        numbers[index + 1] = numbers[index]
    numbers[position] = value

def calculate_sum(numbers: list[int], index: int):
    sum = 0
    for i in range(index):
        sum += numbers[i]
    return sum

def replace_zero_by_rolling_sum(numbers: list[int]):
    for index in range(len(numbers)):
        if numbers[index] == 0:
            numbers[index] = calculate_sum(numbers, index)

def replace_zero_by_rolling_sum(numbers: list[int]):
    rolling_sum = 0
    for index in range(len(numbers)):
        if numbers[index] == 0:
            numbers[index] = rolling_sum
        rolling_sum += numbers[index]
