# pip install treelib
from treelib import Tree


def insert_trie_into_tree(tree: Tree, trie, parent_word: str | None = None):
    if parent_word is None:
        tree.create_node(identifier="root")
        for child in trie.children:
            if child is not None:
                insert_trie_into_tree(tree, child, "root")
    else:
        tree.create_node(identifier=trie.word, parent=parent_word)
        for child in trie.children:
            if child is not None:
                insert_trie_into_tree(tree, child, trie.word)


def visualize_trie(trie):
    tree = Tree()
    insert_trie_into_tree(tree, trie)
    print(tree.show(stdout=False))
