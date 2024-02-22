def find_maximum(numbers: list[int]) -> int:
    maximum = numbers[0]
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum


def calculate_mean(numbers: list[int]) -> float:
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)


def is_twice_in_list(numbers: list[int], number_to_find: int) -> bool:
    for index in range(len(numbers) - 1):
        if numbers[index] == number_to_find and numbers[index + 1] == number_to_find:
            return True
    return False


def add_3_after_5(numbers: list[int]):
    index = 0
    while index < len(numbers):
        if numbers[index] == 5:
            numbers.append(0)
            index_to_move = len(numbers) - 2
            while index_to_move >= index + 1:
                numbers[index_to_move + 1] = numbers[index_to_move]
                index_to_move -= 1
            numbers[index + 1] = 3
        index += 1
