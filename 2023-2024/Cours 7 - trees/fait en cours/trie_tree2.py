from __future__ import annotations

from dataclasses import dataclass
from visualize_tree import visualize_trie


@dataclass
class Trie:
    children: dict[str, Trie]
    is_end_of_word: bool = False


def make_empty_trie() -> Trie:
    return Trie(children={}, is_end_of_word=False)


def insert_word(word: str, trie: Trie):
    node = trie
    for char in word:
        if char not in node.children:
            # create a new child trie
            child = make_empty_trie()
            # declare the child in the parent children
            node.children[char] = child

        node = node.children[char]

    node.is_end_of_word = True


def get_node(prefix: str, trie: Trie) -> Trie | None:
    node = trie
    for char in prefix:
        if char not in node.children:
            return None
        node = node.children[char]
    return node


def get_words(node: Trie, prefix: str) -> list[str]:
    words = []
    if node.is_end_of_word:
        word = prefix
        # ajouter word dans words
        words.append(word)

    for char, child in node.children.items():
        child_words = get_words(child, prefix + char)
        # ajouter tous les chidld_words dans words
        words += child_words
        # words.extend

    return words


def autocomplete(trie: Trie, prefix: str) -> list[str]:
    node = get_node(prefix, trie)
    return get_words(node, prefix)


words = ["apple", "app", "ape", "banana", "bat", "ball"]


trie = make_empty_trie()
insert_word("a", trie=trie)
insert_word("b", trie=trie)
for word in words:
    insert_word(word, trie)
visualize_trie(trie)

print(autocomplete(trie, "ap"))


trie = make_empty_trie()
with open("words_harry_potter.txt") as file:
    words = file.read().split()

for word in words:
    insert_word(word, trie)

print(autocomplete(trie, "e"))
