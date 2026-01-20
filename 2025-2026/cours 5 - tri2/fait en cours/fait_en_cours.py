from __future__ import annotations


def double_list(numbers: list[int]) -> list[int]:
    new_list = []

    for number in numbers:
        new_list.append(number * 2)
    return new_list


def double_list(numbers: list[int]) -> list[int]:
    return [number * 2 for number in numbers]


def check_same_start_end(word: str) -> bool:
    # if word[0]  == word[-2] and word[1] == word[-1]:
    #     return True
    # else:
    #     return False

    # return  word[0]  == word[-2] and word[1] == word[-1]
    if len(word) < 2:
        return False
    return word[:2] == word[-2:]


def get_double_letter_index(word: str) -> int | None:
    # for each index except last
    for index in range(len(word) - 1):
        if word[index] == word[index + 1]:
            return index
    return None


print(list("345"))


def calculate_sum(numbers: list[int]) -> int:
    print(len(numbers))
    if len(numbers) == 1:
        return numbers[0]

    first_element = numbers[0]
    tail = numbers[1:]

    return first_element + calculate_sum(tail)


numbers = [2] * 100

print(calculate_sum(numbers))


def find_zero_index(numbers: list[int]) -> int:
    """O(n)"""
    # for i in range(len(numbers)):
    #     if numbers[i] == 0:
    #         return i

    for i, number in enumerate(numbers):
        if number == 0:
            return i
    return -1


def find_zero_index(numbers: list[int], start_index: int, end_index: int) -> int:
    middle_index = int((start_index + end_index) / 2)

    if numbers[middle_index] == 0:
        return middle_index
    if numbers[middle_index] > 0:
        return find_zero_index(numbers, start_index, middle_index - 1)
    return find_zero_index(numbers, middle_index + 1, end_index)


numbers = [-2, -3, 0, 6, 72, 12, 15]
print(find_zero_index(numbers, 0, len(numbers)))


def fusion(numbers1: list[int], numbers2: list[int]) -> list[int]:
    result = []
    i1 = i2 = 0

    while i1 < len(numbers1) and i2 < len(numbers2):
        if numbers1[i1] <= numbers2[i2]:
            result.append(numbers1[i1])
            i1 += 1
        else:
            result.append(numbers2[i2])
            i2 += 1

    while i1 < len(numbers1):
        result.append(numbers1[i1])
        i1 += 1
    while i2 < len(numbers2):
        result.append(numbers2[i2])
        i2 += 1

    return result


def merge_sort(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers

    limit = len(numbers) // 2

    return fusion(merge_sort(numbers[:limit]), merge_sort(numbers[limit:]))
