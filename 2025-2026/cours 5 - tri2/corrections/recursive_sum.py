def recursive_sum(numbers: list[int]) -> int:
    """
    Recursively computes the sum of all elements in a list of integers.
    """
    # if the list has only one element, return it
    if len(numbers) == 1:
        return numbers[0]
    # Recursive case: sum the first element and the sum of the rest of the list

    first_element = numbers[0]
    rest_of_list = numbers[1:]
    return first_element + recursive_sum(rest_of_list)


example_list = [1, 2, 3, 4]
print(recursive_sum(example_list))  # Output: 10
