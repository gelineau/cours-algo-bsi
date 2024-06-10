from __future__ import annotations

import time
from bs4 import BeautifulSoup
import requests
import re


def extract_text_from_html(url):
    response = requests.get(url)
    response.raise_for_status()
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    # Extract the raw text from the HTML
    text = soup.get_text()
    return text


def get_words(text: str) -> list[str]:
    # Remove punctuation from the text
    text = re.sub(r"[^\w\s]", " ", text)
    # Split the text into words
    words = text.split()
    return words


# url = "https://fr.wikipedia.org/wiki/France"
# raw_text = extract_text_from_html(url)
# with open("france.txt", "w") as file:
#     file.write(raw_text)

with open("france.txt", "r") as file:
    raw_text = file.read()

words = get_words(raw_text)

# keep only long words, avoid unwanted words, change to lowercase
words = [
    word.lower()
    for word in words
    if len(word) >= 8 and word != "consulté" and "fran" not in word
]


def find_more_frequent(words: list[str]) -> str:
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
