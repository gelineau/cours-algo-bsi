from __future__ import annotations

import time
from bs4 import BeautifulSoup
import requests
import re


def read_words_from_file() -> list[str]:
    words = []
    with open("france.txt", "r") as file:
        for line in file:
            words.extend(line.split())

    return words


def find_more_frequent(words: list[str]) -> str:
    """O(n2)"""
    most_frequent_word = None
    max_occurences = 0

    for word in words:
        occurences = 0
        for word_to_check in words:
            if word_to_check == word:
                occurences += 1
        if occurences > max_occurences:
            max_occurences = occurences
            most_frequent_word = word
    return most_frequent_word


def find_more_frequent2(words: list[str]) -> str:
    """O(n.log(n))"""
    words = sorted(words)

    most_frequent_word = None
    max_occurences = 0

    current_word = None
    current_occurence_number = 0
    for word in words:
        if word == current_word:
            current_occurence_number += 1
        else:
            if current_occurence_number > max_occurences:
                max_occurences = current_occurence_number
                most_frequent_word = current_word
            current_word = word
            current_occurence_number = 1

    return most_frequent_word


def find_more_frequent3(words: list[str]) -> str:
    occurences = {}
    for word in words:
        if word in occurences:
            occurences[word] += 1
        else:
            occurences[word] = 1

    max_occurence = 0
    for key, value in occurences.items():
        if value > max_occurence:
            max_occurence = value
            most_frequent_word = key

    return most_frequent_word


words = read_words_from_file()

# n2
start_time = time.time()
print(find_more_frequent(words))
print(time.time() - start_time)

# n log n
start_time = time.time()
print(find_more_frequent2(words))
print(time.time() - start_time)

# O(n)
start_time = time.time()
print(find_more_frequent3(words))
print(time.time() - start_time)
