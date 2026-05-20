from __future__ import annotations

from dataclasses import dataclass
from pprint import pprint

from visualize_tree import visualize_trie


@dataclass
class Trie:
    children: dict[str, Trie]
    word: str | None = None
    # full word stored at end-of-word nodes, None otherwise

    def insert(self: Trie, word: str):
        current = self
        for letter in word:
            if letter in current.children:
                current = current.children[letter]
            else:
                child = Trie(children={}, word=None)
                current.children[letter] = child
                current = current.children[letter]
        current.word = word

    def find_node(self, prefix: str) -> Trie | None:
        current = self
        for letter in prefix:
            if letter in current.children:
                current = current.children[letter]
            else:
                return None
        return current

    def find_words(self: Trie) -> list[str]:
        results = []
        if self.word is not None:
            results.append(self.word)

        for letter, child in self.children.items():
            words_for_child = child.find_words()
            results.extend(words_for_child)
        return results

    def autocomplete(self, prefix: str) -> list[str]:
        node = self.find_node(prefix)
        if node is None:
            return []
        return node.find_words()


root = Trie({})
root.insert("app")
root.insert("ape")
root.insert("apple")
root.insert("bat")
root.insert("ban")
root.insert("bank")
visualize_trie(root)
# pprint(root)
