from __future__ import annotations

import sys
from dataclasses import dataclass
from visualize_tree import visualize_trie


@dataclass
class Trie:
    children: dict[str, Trie]
    word: str | None = None
    # full word stored at end-of-word nodes, None otherwise

    def insert(self: Trie, word: str):
        node = self
        for character in word:
            if character not in node.children:
                node.children[character] = Trie(children={})
            node = node.children[character]
        node.word = word

    def find_node(self: Trie, prefix: str) -> Trie | None:
        node = self
        for character in prefix:
            if character not in node.children:
                return None
            node = node.children[character]
        return node

    def find_words(self: Trie) -> list[str]:
        words = []
        if self.word is not None:
            words.append(self.word)
        for char, child in self.children.items():
            child_words = child.find_words()
            words.extend(child_words)
        return words

    def autocomplete_all(self: Trie, prefix: str) -> list[str]:
        node = self.find_node(prefix)
        if node is None:
            return []
        return node.find_words()


trie = Trie(children={})
trie.insert("apple")
trie.insert("app")
trie.insert("banana")
trie.insert("bat")
trie.insert("batman")

print(f"{trie.autocomplete_all("app")=}")  # Output: ['app', 'apple']
print(f"{trie.autocomplete_all("ba")=}")  # Output: ['banana', 'bat', 'batman']
visualize_trie(trie)

#
# ##############
#
filename = "words_harry_potter.txt"
with open(filename) as file:
    words = file.read().split()

trie = Trie(children={})
for word in words:
    trie.insert(word)

visualize_trie(trie)

prefix = "rep"
print(f"Autocomplete suggestions for prefix {prefix=}")

print(trie.autocomplete_all(prefix))
