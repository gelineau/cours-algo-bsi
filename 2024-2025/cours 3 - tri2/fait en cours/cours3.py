# def find_zero_index(numbers: list[int]) -> int:
#     """
#     Exo 1.1
#     """
#     for index in range(len(numbers)):
#         value = numbers[index]
#         if value == 0:
#             return index
#
#
# # O(n)
#
#
# def find_zero_index_recursive(
#     numbers: list[int], start_index: int, end_index: int
# ) -> int:
#     print(start_index, end_index)
#     """
#     Exo 1.2
#     """
#     middle_index = int((start_index + end_index) / 2)
#     value = numbers[middle_index]
#
#     if value == 0:
#         return middle_index
#
#     if value > 0:
#         result = find_zero_index_recursive(numbers, start_index, middle_index - 1)
#         return result
#
#     result = find_zero_index_recursive(numbers, middle_index + 1, end_index)
#     return result
#
#
# numbers = [-2, -3, 0, 6, 72, 12, 15]
#
# print(f"{find_zero_index(numbers)=}")
# print(f"{find_zero_index_recursive(numbers, 0, len(numbers)-1)=}")


def merge(numbers_a: list[int], numbers_b: list[int]) -> list[int]:
    result = []
    index_a = index_b = 0

    while index_a <= len(numbers_a) - 1 and index_b <= len(numbers_b) - 1:
        if numbers_a[index_a] <= numbers_b[index_b]:
            result.append(numbers_a[index_a])
            index_a += 1
        else:
            result.append(numbers_b[index_b])
            index_b += 1

    while index_a <= len(numbers_a) - 1:
        result.append(numbers_a[index_a])
        index_a += 1

    while index_b <= len(numbers_b) - 1:
        result.append(numbers_b[index_b])
        index_b += 1

    return result


def merge_sort(numbers: list[int]) -> list[int]:
    if len(numbers) <= 1:
        return numbers

    middle_index = int(len(numbers) / 2)

    numbers_a = numbers[:middle_index]
    numbers_b = numbers[middle_index:]

    sorted_a = merge_sort(numbers_a)
    sorted_b = merge_sort(numbers_b)

    return merge(sorted_a, sorted_b)


numbers_a = [1, 4, 8]
numbers_b = [6, 7, 12, 15]
print(merge(numbers_a, numbers_b))

print(merge_sort([3, 7, 1, 8, 1, 14, 42, 25]))
