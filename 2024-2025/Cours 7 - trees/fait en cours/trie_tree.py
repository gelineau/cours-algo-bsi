from __future__ import annotations

from dataclasses import dataclass

from visualize_tree import visualize_trie


@dataclass
class Trie:
    children: list[Trie | None]  # a list of 256 children, possibly None
    word: str
    is_end_of_word: bool = False


def create_empty_trie() -> Trie:
    return Trie(children=[None] * 256, word="", is_end_of_word=False)


def insert_letter_into_trie(one_letter_word: str, trie: Trie):
    code = ord(one_letter_word)
    if trie.children[code] == None:
        child = Trie(children=[None] * 256, word=one_letter_word, is_end_of_word=False)
        # child = create_empty_trie()
        # child.word = one_letter_word
        trie.children[code] = child


def insert_word_into_trie(word: str, trie: Trie):
    node = trie
    for character in word:
        code = ord(character)
        if node.children[code] == None:
            child = create_empty_trie()
            child.word = node.word + character
            node.children[code] = child
        node = node.children[code]
    node.is_end_of_word = True


def insert_word_into_trie(word: str, node: Trie):  # recursive
    character = word[0]
    code = ord(character)
    if node.children[code] == None:
        child = create_empty_trie()
        child.word = node.word + character
        node.children[code] = child

    if len(word) > 1:
        insert_word_into_trie(word[1:], node.children[code])
    else:
        node.children[code].is_end_of_word = True


def find_node(trie: Trie, prefix: str) -> Trie | None:
    node = trie
    for character in prefix:
        code = ord(character)
        node = node.children[code]
        if node == None:
            return None
    return node


def find_words(trie: Trie) -> list[str]:
    words = []
    if trie.is_end_of_word:
        words.append(trie.word)

    for child in trie.children:
        if child != None:
            words_for_child = find_words(child)
            words.extend(words_for_child)

    return words


def autocomplete(trie: Trie, prefix: str) -> list[str]:
    node = find_node(trie, prefix)
    return find_words(node)


#
# trie = create_empty_trie()
# for word in ("app", "apple", "ape", "bat", "bank", "ban"):
#     insert_word_into_trie(word, trie)
# visualize_trie(trie)
#
# print(autocomplete(trie, "ap"))


# pip install treelib


trie = create_empty_trie()
filename = "words_harry_potter.txt"
with open(filename) as file:
    words = file.read().split()

for word in words:
    insert_word_into_trie(word, trie)

# visualize_trie(trie)


print(autocomplete(trie, "exp"))
