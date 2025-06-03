

#
# def calculate_occurence_number(numbers: list[int], number_to_find: int)-> int:
#
#
# def filter_lower_numbers(numbers: list[int], limit: int) -> list[int]:
#

def count_zeros(numbers: list[int]) -> int:
    count = 0
    for number in numbers:
    # for i in range(len(numbers)):
    #     if numbers[i] == 0

    # i = 0
    # while i < len(numbers):
    #     ...
    #     i += 1


        if number == 0:
            count += 1
    return count
# O(n)

def calculate_mean(numbers: list[int]) -> float:
    if len(numbers) == 0:
    if not numbers:
        raise ValueError("mean of empty list")

    sum = 0
    for number in numbers:
        sum += number

    return sum / len(numbers)
# O(n)

def search_value_twice(numbers: list[int], searched_value: int) -> bool:
    for i in range(len(numbers)-1):
        if numbers[i] == searched_value and numbers[i+1] == searched_value:
            return True
    return False

    # O(n)


def search_value_twice(numbers: list[int], value: int) -> bool:
    previous_value = None
    for number in numbers:
        if previous_value == number and value== number:
            return True
        previous_value = number

    return False

    # O(n)

    #
    # for number1, number2 in zip(numbers, numbers[1:]):
    #     if number1 == number2:
    #         return True
    #
    # numbers      2 3 0 0 5 4
    # numbers[1:]  3 0 0 5 4

def add_threes(input_list: list[int]):
    index = 0
    while index < len(input_list):
        if input_list[index] == 5:
            array_length = len(input_list)
            input_list.append(0)

            index_to_move = array_length - 1
            while index_to_move >= index + 1:
                input_list[index_to_move+1] = input_list[index_to_move]
                index_to_move -= 1

            input_list[index + 1 ] = 3
        index += 1

