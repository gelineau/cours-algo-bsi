def find_minimum_index(numbers: list[int], start_index: int) -> int:
    min_index = start_index
    min_value = numbers[start_index]

    for search_index in range(start_index, len(numbers)):
        search_value = numbers[search_index]

        if search_value < min_value:
            min_index = search_index
            min_value = search_value

    return min_index


def swap(numbers: list[int], index1: int, index2: int):
    # temp = numbers[index1]
    # numbers[index1] = numbers[index2]
    # numbers[index2] = temp
    numbers[index1], numbers[index2] = numbers[index2], numbers[index1]


def selection_sort(numbers: list[int]):
    for current_index in range(0, len(numbers) - 1):
        min_index = find_minimum_index(numbers, current_index)
        swap(numbers, min_index, current_index)


def insertion_sort(numbers: list[int]):
    for index_to_sort in range(1, len(numbers)):
        index_to_move = index_to_sort - 1
        value_to_sort = numbers[index_to_sort]
        while numbers[index_to_move] > value_to_sort and index_to_move >= 0:
            numbers[index_to_move + 1] = numbers[index_to_move]
            index_to_move -= 1

        numbers[index_to_move + 1] = value_to_sort


numbers = [1, 6, 9, 4, 8]
print(f"la valeur est {find_minimum_index(numbers, 1)=}")
numbers = [9, 6, 1, 4, 8]
insertion_sort(numbers)
print(f"{numbers=}")
