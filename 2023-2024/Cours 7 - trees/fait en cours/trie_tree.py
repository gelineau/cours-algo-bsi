from __future__ import annotations

from dataclasses import dataclass
from visualize_tree import visualize_trie


@dataclass
class Trie:
    children: list[Trie | None]  # a list of 256 children, possibly None
    word: str
    is_end_of_word: bool = False


def make_empty_trie() -> Trie:
    return Trie(children=256 * [None], word="", is_end_of_word=False)


def insert_word(word: str, trie: Trie):
    node = trie
    for char in word:
        index = ord(char)
        if node.children[index] is None:
            # create a new child trie
            child = make_empty_trie()
            child.word = node.word + char
            # declare the child in the parent children
            node.children[index] = child

        node = node.children[index]

    node.is_end_of_word = True


def get_node(prefix: str, trie: Trie) -> Trie | None:
    node = trie
    for char in prefix:
        index = ord(char)
        if node.children[index] is None:
            return None
        node = node.children[index]
    return node


def get_words(node: Trie) -> list[str]:
    words = []
    if node.is_end_of_word:
        word = node.word
        # ajouter word dans words
        words.append(word)

    for child in node.children:
        if child is not None:
            child_words = get_words(child)
            # ajouter tous les chidld_words dans words
            words += child_words
            # words.extend

    return words


def autocomplete(trie: Trie, prefix: str) -> list[str]:
    node = get_node(prefix, trie)
    return get_words(node)


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
