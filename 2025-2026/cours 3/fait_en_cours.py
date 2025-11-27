from __future__ import annotations

import hashlib
from pprint import pprint


def check_characters(word: str) -> str:
    if word[1] == word[-1]:
        return "OK"
    else:
        return "KO"


def check_characters(word: str) -> str:
    if word[1] == word[-1]:
        return "OK"
    return "KO"


def double_numbers(numbers: list[int | str]) -> list[int | str]:
    new_list = []
    for number in numbers:
        new_list.append(number * 2)
    return new_list


def double_numbers(numbers: list[int | str]) -> list[int | str]:
    return [number * 2 for number in numbers]


print(double_numbers([1, 2, 4]))
print(double_numbers(["1", "2", "4"]))


def find_word_position(word_to_find: str, words: list[str]) -> int | None:
    for i in range(len(words)):
        word = words[i]
        if word == word_to_find:
            return i
    return None


def find_word_position(word_to_find: str, words: list[str]) -> int | None:
    for i, word in enumerate(words):
        if word == word_to_find:
            return i
    return None


def combinatate_strings(string1: str, string2: str) -> list[str]:
    result = []
    for character1 in string1:
        for character2 in string2:
            result.append(character1 + character2)
    return result


def combinatate_strings(string1: str, string2: str) -> list[str]:
    return [character1 + character2 for character1 in string1 for character2 in string2]


def summarize_file(file_path: str) -> list[tuple[int, int, str]]:
    summaries = []
    with open(file_path) as f:
        for line in f:
            num_characters = len(line)
            words = line.split()
            num_words = len(words)
            md5 = hashlib.md5(line.encode("utf-8")).hexdigest()
            summaries.append((num_characters, num_words, md5))
    return summaries


# md5 = hashlib.md5(line.encode("utf-8")).hexdigest()
# summaries.append({"num_chars": num_characters, "num_words": num_words, "md5": md5})

summaries = summarize_file("fait_en_cours.py")
save_summary(summaries)
