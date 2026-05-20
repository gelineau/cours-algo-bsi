from __future__ import annotations

import pytest

from trie import Trie


def test_insert_single_letter_word():
    trie = Trie(children={})
    trie.insert("a")
    assert len(trie.children) == 1
    assert trie.children["a"].word == "a"
    assert trie.children["a"].children == {}


def test_insert_word():
    trie = Trie(children={})
    trie.insert("bat")
    assert trie.children["b"].word is None
    assert trie.children["b"].children["a"].word is None
    assert trie.children["b"].children["a"].children["t"].word == "bat"
    assert trie.children["b"].children["a"].children["t"].children == {}


def test_insert_two_words_with_common_prefix():
    trie = Trie(children={})
    trie.insert("bat")
    trie.insert("ban")
    assert len(trie.children) == 1
    node_b = trie.children["b"]
    assert len(node_b.children) == 1
    node_a = node_b.children["a"]
    assert len(node_a.children) == 2
    assert node_a.children["t"].word == "bat"
    assert node_a.children["n"].word == "ban"


def test_insert_empty_word():
    trie = Trie(children={})
    trie.insert("")
    assert len(trie.children) == 0


def test_insert_integer():
    trie = Trie(children={})
    with pytest.raises(TypeError):
        trie.insert(24)


def test_find_node_existing_prefix():
    trie = Trie(children={})
    trie.insert("apple")
    trie.insert("app")
    node = trie.find_node("app")
    assert node == trie.children["a"].children["p"].children["p"]


def test_find_node_missing_prefix():
    trie = Trie(children={})
    trie.insert("apple")
    node = trie.find_node("xyz")
    assert node is None


def test_find_words():
    trie = Trie(children={})
    trie.insert("app")
    trie.insert("apple")
    trie.insert("ape")
    trie.insert("bank")
    node = trie.children["a"].children["p"]
    assert sorted(node.find_words()) == ["ape", "app", "apple"]


def test_autocomplete_all_with_matching_prefix():
    trie = Trie(children={})
    trie.insert("app")
    trie.insert("apple")
    trie.insert("ape")
    trie.insert("bat")
    assert sorted(trie.autocomplete_all("ap")) == ["ape", "app", "apple"]


def test_autocomplete_all_with_missing_prefix():
    trie = Trie(children={})
    trie.insert("app")
    trie.insert("apple")
    assert trie.autocomplete_all("xyz") == []


def test_autocomplete_all_with_exact_word_as_prefix():
    trie = Trie(children={})
    trie.insert("ban")
    trie.insert("bank")
    assert sorted(trie.autocomplete_all("ban")) == ["ban", "bank"]
