from __future__ import annotations

import itertools
import sys
from dataclasses import dataclass
from typing import Dict


@dataclass
class Trie:
    children: dict[str, Trie]  # key is next letter
    is_end_of_word: bool = False


def make_empty_trie() -> Trie:
    return Trie(children={}, is_end_of_word=False)


def insert(trie: Trie, word: str):
    node = trie
    for character in word:
        if character not in node.children:
            node.children[character] = make_empty_trie()
        node = node.children[character]
    node.is_end_of_word = True


def find_node(trie: Trie, prefix: str) -> Trie | None:
    node = trie
    for char in prefix:
        if char not in node.children:
            return None
        node = node.children[char]
    return node


def search(trie: Trie, word: str) -> bool:
    node = find_node(trie, word)
    return node is not None and node.is_end_of_word


def find_words(trie: Trie, prefix: str) -> list[str]:
    words = []
    if trie.is_end_of_word:
        words.append(prefix)
    for char, child in trie.children.items():
        child_words = find_words(child, prefix + char)
        words.extend(child_words)
    return words


def autocomplete_all(trie: Trie, prefix: str) -> list[str]:
    node = find_node(trie, prefix)
    return find_words(node, prefix)


trie = make_empty_trie()
insert(trie, "apple")
insert(trie, "app")
insert(trie, "banana")
insert(trie, "bat")
insert(trie, "batman")

print(autocomplete_all(trie, "app"))  # Output: ['app', 'apple']
print(autocomplete_all(trie, "ba"))  # Output: ['banana', 'bat', 'batman']


words = ["a" * 200 + str(n) for n in range(10000)]
print(words)
print(len(words))


print(f"{sys.getsizeof(words) + sum(sys.getsizeof(word) for word in words)=}")

trie = make_empty_trie()
for word in words:
    insert(trie, word)


def get_sizeof_trie(trie: Trie):
    return (
        sys.getsizeof(trie)
        + sys.getsizeof(trie.children)
        + sum(get_sizeof_trie(child) for child in trie.children.values())
    )


print(f"{get_sizeof_trie(trie)=}")
