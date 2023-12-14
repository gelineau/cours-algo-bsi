def find_index_of_zero(numbers: list[int]) -> int:
    index = 0
    for number in numbers:
        if number == 0:
            return index
        index += 1


numbers = [-2, -3, 0, 6, 72, 12, 15]

# print(f"{find_index_of_zero(numbers)=}")


def find_zero_recursive(numbers: list[int], start_index: int, end_index: int) -> int:
    middle_index = (start_index + end_index) // 2

    middle_value = numbers[middle_index]

    if middle_value < 0:
        return find_zero_recursive(numbers, middle_index + 1, end_index)
    if middle_value > 0:
        return find_zero_recursive(numbers, start_index, middle_index - 1)
    return middle_index


def find_zero_fast(numbers: list[int]) -> int:
    return find_zero_recursive(numbers, 0, len(numbers) - 1)


# print(f"{find_zero_fast(numbers)=}")


def merge(numbers1: list[int], numbers2: list[int]) -> list[int]:
    index1 = index2 = 0
    result = []

    while index1 < len(numbers1) and index2 < len(numbers2):
        if numbers1[index1] < numbers2[index2]:
            result.append(numbers1[index1])
            index1 += 1
        else:
            result.append(numbers2[index2])
            index2 += 1

    while index1 < len(numbers1):
        result.append(numbers1[index1])
        index1 += 1

    while index2 < len(numbers2):
        result.append(numbers2[index2])
        index2 += 1

    return result


numbers1 = [2, 4, 6, 8, 10, 12]
numbers2 = [1, 3, 5]

print(f"{merge(numbers1, numbers2)=}")


def merge_sort(numbers: list[int]) -> list[int]:
    # 0
    if len(numbers) <= 1:
        return numbers

    middle_index = len(numbers) // 2

    numbers1 = numbers[:middle_index]
    numbers2 = numbers[middle_index:]
    sorted_numbers1 = merge_sort(numbers1)
    sorted_numbers2 = merge_sort(numbers2)

    return merge(sorted_numbers1, sorted_numbers2)


numbers = [8, 4, 1, 15, 7, 12, 16]
print(f"{merge_sort(numbers)}")
