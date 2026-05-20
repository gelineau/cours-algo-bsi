from __future__ import annotations
import sys
from dataclasses import dataclass


@dataclass
class Trie:
    children: dict[str, Trie]
    is_end_of_word: bool = False

    def insert(self: Trie, word: str) -> None:
        node = self
        for character in word:
            if character not in node.children:
                node.children[character] = Trie(children={})
            node = node.children[character]
        node.is_end_of_word = True

    def find_node(self: Trie, prefix: str) -> Trie | None:
        node = self
        for character in prefix:
            if character not in node.children:
                return None
            node = node.children[character]
        return node

    def find_words(self: Trie, prefix: str) -> list[str]:
        words = []
        if self.is_end_of_word:
            words.append(prefix)
        for character, child in self.children.items():
            words.extend(child.find_words(prefix + character))
        return words

    def autocomplete_all(self: Trie, prefix: str) -> list[str]:
        node = self.find_node(prefix)
        if node is None:
            return []
        return node.find_words(prefix)


trie = Trie(children={})
trie.insert("apple")
trie.insert("app")
trie.insert("banana")
trie.insert("bat")
trie.insert("batman")

print(f"{trie.autocomplete_all("app")=}")  # Output: ['app', 'apple']
print(f"{trie.autocomplete_all("ba")=}")  # Output: ['banana', 'bat', 'batman']


##############

filename = "words_harry_potter.txt"
with open(filename) as file:
    words = file.read().split()

trie = Trie(children={})
for word in words:
    trie.insert(word)


prefix = "rep"
print(f"Autocomplete suggestions for prefix {prefix=}")

print(trie.autocomplete_all(prefix))

###################

words = ["a" * 200 + str(n) for n in range(10000)]
# print(words)
# print(len(words))


print(f"{sys.getsizeof(words) + sum(sys.getsizeof(word) for word in words)=}")

trie = Trie(children={})
for word in words:
    trie.insert(word)


def get_sizeof_trie(trie: Trie):
    return (
        sys.getsizeof(trie)
        + sys.getsizeof(trie.children)
        + sum(sys.getsizeof(key) for key in trie.children.keys())
        + sum(get_sizeof_trie(child) for child in trie.children.values())
    )


print(f"{get_sizeof_trie(trie)=}")
