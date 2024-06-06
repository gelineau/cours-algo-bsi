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


start_time = time.time()

# call function here
# ...

print(time.time() - start_time)
