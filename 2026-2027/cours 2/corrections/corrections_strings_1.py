from __future__ import annotations


def get_first_characters(sentence: str, number: int) -> str:
    # Slices never raise an IndexError, even if number > len(sentence)
    return sentence[:number]


print(get_first_characters("Python", 3))  # Pyt
print(get_first_characters("Python", 10))  # Python (no error)
print(get_first_characters("Python", 0))  # ""


def count_letter_a_in_second_word(sentence: str) -> int:
    # Split the sentence into words
    words = sentence.split()
    second_word = words[1]
    # Count the number of "a" (case sensitive)
    return second_word.count("a")


print(count_letter_a_in_second_word("bonjour ananas monde"))  # 3
print(count_letter_a_in_second_word("bonjour Ananas monde"))  # 2
print(count_letter_a_in_second_word("bonjour chat monde"))  # 1
print(count_letter_a_in_second_word("bonjour python monde"))  # 0


def trim_second_to_last_word(sentence: str) -> str:
    # Split the sentence into words
    words = sentence.split()
    # Get the second to last word using a negative index
    second_to_last_word = words[-2]
    # Remove the first two and last two characters using slices
    return second_to_last_word[2:-2]


print(trim_second_to_last_word("bonjour python monde bonsoir"))  # tho
print(trim_second_to_last_word("un abcdefgh deux trois"))  # cdef


def get_last_word_as_integer(sentence: str) -> int:
    # Split the sentence and get the last word using a negative index
    last_word = sentence.split()[-1]
    # int() will raise a ValueError if the word is not a valid number
    return int(last_word)


print(get_last_word_as_integer("il fait 42"))  # 42
print(get_last_word_as_integer("le score est 100"))  # 100
print(get_last_word_as_integer("bonjour monde"))  # ❌ ValueError


def get_last_characters_uppercase(sentence: str, number: int) -> str:
    # Convert the sentence to uppercase
    uppercased = sentence.upper()
    # Pad with spaces on the left to ensure the string is at least n characters long
    padded = " " * number + uppercased
    # Return the last n characters using a slice
    return padded[-number:]


print(get_last_characters_uppercase("Python", 3))  # "HON"
print(get_last_characters_uppercase("Hi", 5))  # "   HI"
print(get_last_characters_uppercase("Python", 10))  # "    PYTHON"


def replace_with_stars(sentence: str) -> str:
    # Repeat "*" as many times as the length of the sentence
    return "*" * len(sentence)


print(replace_with_stars("Python"))  # ******
print(replace_with_stars("Bonjour"))  # *******
print(replace_with_stars(""))  # ""


def get_first_characters_with_repeat(sentence: str, number: int) -> str:
    # Repeat the sentence n times, which is more than necessary but guarantees
    # that the resulting string is at least n characters long
    repeated_sentence = sentence * number
    # Return the first n characters
    return repeated_sentence[:number]


print(get_first_characters_with_repeat("Python", 3))  # Pyt
print(get_first_characters_with_repeat("Python", 10))  # PythonPyth
print(get_first_characters_with_repeat("ab", 7))  # abababa
