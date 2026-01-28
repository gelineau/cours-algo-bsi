######################################
# 1. Count vowels in a string
# Write a function that takes a string as input and returns the number of vowels (a, e, i, o, u, y) it contains.
######################################


def count_vowels(s: str) -> int:
    vowels = "aeiouyAEIOUY"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


######################################
# 2. Extract even elements from a list
# Write a function that takes a list of numbers and returns a new list containing only the even elements.
######################################


# Version with a for loop
def extract_evens(numbers: list[int]) -> list[int]:
    result = []
    for number in numbers:
        if number % 2 == 0:
            result.append(number)
    return result


# Version with a list comprehension
def extract_evens(numbers: list[int]) -> list[int]:
    return [number for number in numbers if number % 2 == 0]


######################################
# 3. Find the largest gap between consecutive elements
# Write a function that takes a list of numbers and returns the largest difference between two consecutive elements.
######################################


def find_largest_gap(numbers: list[int]) -> int:
    if len(numbers) < 2:
        return 0
    max_gap = 0
    for i in range(len(numbers) - 1):
        gap = numbers[i + 1] - numbers[i]
        if gap > max_gap:
            max_gap = gap
    return max_gap


######################################
# 4. Reverse a list of integers
# Write a function that takes a list as input and returns a new list with the same elements in reverse order.
######################################


def reverse_list(numbers: list[int]) -> list[int]:
    return numbers[::-1]


# Using the built-in reversed() function and list
def reverse_list_reversed(numbers: list[int]) -> list[int]:
    # Returns a new list that is the reverse of numbers
    return list(reversed(numbers))


# 3. Using a for loop (building a new list)
def reverse_list_loop(numbers: list[int]) -> list[int]:
    # Returns a new list that is the reverse of numbers
    result = []
    for i in range(len(numbers)):
        result.append(numbers[len(numbers) - 1 - i])
    return result


# 4. Using a while loop
def reverse_list_while(numbers: list) -> list:
    # Returns a new list that is the reverse of numbers
    result = []
    i = len(numbers) - 1
    while i >= 0:
        result.append(numbers[i])
        i -= 1
    return result


def reverse_list_insert(numbers: list) -> list:
    # Build a new list by inserting each value at the beginning
    # O(n2)
    result = []
    for number in numbers:
        result.insert(0, number)  # Insert each value at the start of the result list
    return result


######################################
# 5. Replace all occurrences of an element
# Write a function that takes a list, an element to replace, and a new element, and returns a new list where all occurrences of the old element are replaced by the new one.
######################################


# Version with a for loop
def replace_all(numbers: list[int], old: int, new: int) -> list[int]:
    result = []
    for number in numbers:
        if number == old:
            result.append(new)
        else:
            result.append(number)
    return result


# Version with a list comprehension
def replace_all(numbers: list[int], old: int, new: int) -> list[int]:
    return [new if number == old else number for number in numbers]


######################################
# 6. Find the index of the smallest element
# Write a function that takes a list of numbers and returns the index of the smallest element.
######################################


def index_of_smallest(numbers: list[int]) -> int:
    if not numbers:
        return -1
    min_index = 0
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[min_index]:
            min_index = i
    return min_index


######################################
# 7. Remove duplicates from a list
# Write a function that takes a list as input and returns a new list without duplicates, preserving the original order.
######################################


def remove_duplicates(numbers: list[int]) -> list[int]:
    result = []
    for item in numbers:
        if item not in result:
            result.append(item)
    return result


######################################
# 8. Merge two lists alternately
# Write a function that takes two lists of the same length and returns a new list with elements alternated.
######################################


def merge_alternate(numbers1: list[int], numbers2: list[int]) -> list[int]:
    result = []
    for i in range(len(numbers1)):
        result.append(numbers1[i])
        result.append(numbers2[i])
    return result


######################################
# 9. Count words in a sentence
# Write a function that takes a string (sentence) and returns the number of words (words are separated by spaces).
######################################


def count_words(sentence: str) -> int:
    return len(sentence.split())
