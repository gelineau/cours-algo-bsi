from __future__ import annotations

# pip install bs4
# pip install requests
import time
from bs4 import BeautifulSoup
import requests
import re


def extract_text_from_html_page(url):
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


url = "https://fr.wikipedia.org/wiki/France"
raw_text = extract_text_from_html_page(url)
words = get_words(raw_text)

# keep only long words, avoid unwanted words, change to lowercase
words = [
    word.lower()
    for word in words
    if len(word) >= 8 and word != "consulté" and "fran" not in word
]

words = 10 * words


def get_most_frequent_word(words: list[str]) -> str:
    maximum_found = 0
    word_for_maximum = None

    for word in words:
        # calculate the number of occurence of word
        nb_occurences = 0
        for word_to_compare in words:
            if word == word_to_compare:
                nb_occurences += 1
        if nb_occurences > maximum_found:
            maximum_found = nb_occurences
            word_for_maximum = word
        # print(word, nb_occurences)
    return word_for_maximum


def get_most_frequent_word2(words: list[str]) -> str:
    words = sorted(words)
    maximum_found = 0
    word_for_maximum = None

    current_word = None
    current_occurence_number = 0

    for word in words:
        if word == current_word:
            current_occurence_number += 1
        else:
            if current_occurence_number > maximum_found:
                maximum_found = current_occurence_number
                word_for_maximum = current_word
            current_word = word
            current_occurence_number = 1

    return word_for_maximum


def get_most_frequent_word3(words: list[str]) -> str:
    occurences = {}
    maximum_found = 0
    word_for_maximum = None
    for word in words:
        # is word already in occurences
        if word in occurences:
            occurences[word] = occurences[word] + 1
        else:
            occurences[word] = 1

        if occurences[word] > maximum_found:
            maximum_found = occurences[word]
            word_for_maximum = word

    return word_for_maximum


# start_time = time.time()
# # call function here
# print(get_most_frequent_word(words))
# print(time.time() - start_time)

start_time = time.time()
# O(nlog(n))
print(get_most_frequent_word2(words))
print(time.time() - start_time)

start_time = time.time()
# call function here
print(get_most_frequent_word3(words))
print(time.time() - start_time)

print(globals())
