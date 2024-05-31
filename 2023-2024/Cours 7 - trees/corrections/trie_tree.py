from __future__ import annotations

import time
from dataclasses import dataclass
from visualize_tree import visualize_trie


@dataclass
class Trie:
    children: list[Trie | None]  # a list of 256 children, possibly None
    word: str
    is_end_of_word: bool = False


def make_empty_trie() -> Trie:
    return Trie(children=[None] * 256, is_end_of_word=False, word="")


# def insert(trie: Trie, word: str):
#     node = trie
#     for character in word:
#         index = ord(character)
#         if index >= 256:
#             raise ValueError("this character : '{character}' is not allowed")
#         if node.children[index] is None:
#             node.children[index] = make_empty_trie()
#             node.children[index].word = node.word + character
#         node = node.children[index]
#     node.is_end_of_word = True


def insert(node: Trie, word: str):
    """
    Version récursive
    """
    character = word[0]
    index = ord(character)
    if index >= 256:
        raise ValueError("this character : '{character}' is not allowed")
    if node.children[index] is None:
        node.children[index] = make_empty_trie()
        node.children[index].word = node.word + character
    if len(word) == 1:
        node.children[index].is_end_of_word = True
    else:
        insert(node.children[index], word[1:])


def find_node(trie: Trie, prefix: str) -> Trie | None:
    node = trie
    for char in prefix:
        index = ord(char)
        node = node.children[index]
        if node is None:
            return None
    return node


def search(trie: Trie, word: str) -> bool:
    node = find_node(trie, word)

    return node is not None and node.is_end_of_word


def find_words(trie: Trie) -> list[str]:
    words = []
    if trie.is_end_of_word:
        words.append(trie.word)
    for child in trie.children:
        if child is not None:
            words.extend(find_words(child))
    return words


def autocomplete_all(trie: Trie, prefix: str) -> list[str]:
    node = find_node(trie, prefix)
    return find_words(node)


words = ["apple", "app", "ape", "banana", "bat", "ball"]


trie = make_empty_trie()
for word in words:
    insert(trie, word)

visualize_trie(trie)

print(f"{search(trie, 'apple')=} {search(trie, 'appl')=}")

prefix = "ba"
print(f"Autocomplete suggestions for prefix {prefix=}")
print(autocomplete_all(trie, prefix))


filename = "words_harry_potter.txt"
with open(filename) as file:
    words = file.read().split()

trie = make_empty_trie()
for word in words:
    insert(trie, word)

visualize_trie(trie)

prefix = "rep"
print(f"Autocomplete suggestions for prefix {prefix=}")

print(autocomplete_all(trie, prefix))
