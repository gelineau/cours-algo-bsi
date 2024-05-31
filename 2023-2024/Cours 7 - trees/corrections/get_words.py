from __future__ import annotations

# pip install bs4
# pip install requests
import time
from bs4 import BeautifulSoup
import requests
import re

# url = "https://fr.wikipedia.org/wiki/France"
url = "https://fr.vikidia.org/wiki/Sortil%C3%A8ges_dans_Harry_Potter"
filename = "words.txt"


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


raw_text = extract_text_from_html_page(url)
words = get_words(raw_text)

# change to lowercase, remove words with special characters
words = {word.lower() for word in words if all(0 <= ord(char) <= 255 for char in word)}

with open(filename, "w") as file:
    for word in words:
        file.write(word + "\n")
