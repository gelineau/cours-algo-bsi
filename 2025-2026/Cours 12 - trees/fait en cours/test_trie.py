from __future__ import annotations

import pytest

from trie import Trie


def test_insert_single_letter_word():
    trie = Trie(children={})
    trie.insert("a")
    assert len(trie.children) == 1
    assert trie.children["a"].word == "a"
    assert trie.children["a"].children == {}


def test_insert_multiple_letter_word():
    trie = Trie(children={})
    trie.insert("abc")
    assert trie.children["a"].children["b"].children["c"].word == "abc"


def test_insert_multiple_words():
    trie = Trie(children={})
    trie.insert("abb")
    trie.insert("abc")
    assert trie.children["a"].children["b"].children["c"].word == "abc"


def test_insert_empty_word():
    trie = Trie(children={})
    trie.insert("")
    assert trie.children == {}


# def test_insert_number():
#     trie = Trie(children={})
#     with pytest.raises(TypeError):
#         trie.insert(27)


def test_find_node_existing_prefix():
    trie = Trie(children={})
    trie.insert("bank")
    trie.insert("badboy")
    node = trie.find_node("ba")
    assert node == trie.children["b"].children["a"]


def test_find_words():
    trie = Trie(children={})
    trie.insert("app")
    trie.insert("apple")
    trie.insert("ape")
    trie.insert("bat")
    trie.insert("ban")
    trie.insert("bank")
    trie.insert("beurk")

    node = trie.find_node("ba")
    words = node.find_words()
    assert words == ["bat", "ban", "bank"]
