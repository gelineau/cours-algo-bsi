# my_ist = [1, 2, 3]
# print(my_ist)
# my_ist.append(4)
# print(my_ist)
# my_ist.append([5, 6])
# print(my_ist)
# my_ist.extend([5, 6])
# print(my_ist)
####################

# devoir numéro 1


def get_second_character(string: str) -> str:
    return string[1]


# devoir numéro 2
def fetch_first_n_characters(string: str, n: int) -> str:
    return string[:n]


# devoir numéro 3
def make_doubled_list(numbers: list[int]) -> list[int]:
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


def make_doubled_list(numbers: list[int]) -> list[int]:
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i] * 2)
    return result


def make_doubled_list(numbers: list[int]) -> list[int]:
    return [number * 2 for number in numbers]


def count_a_in_second_word(sentence: str, character_to_find: str) -> int:
    words = sentence.split()
    second_word = words[1]
    # return second_word.count("a")
    number_of_a = 0
    for character in second_word:
        if character == character_to_find:
            # number_of_a = number_of_a + 1
            number_of_a += 1
    return number_of_a


print(count_a_in_second_word("bonjour ananas monde", "a"))


def get_last_characters_uppercased(word: str, size: int) -> str:
    uppercased = word.upper()
    # cut_word = uppercased[-size:]
    # if len(cut_word) < size:
    #     result = (size - len(cut_word)) * " " + cut_word
    # else:
    #     result = cut_word
    # return result
    return (" " * size + uppercased)[-size:]


print(get_last_characters_uppercased("chien", 3))
print(get_last_characters_uppercased("chien", 30))
