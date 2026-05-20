# pip install treelib
from treelib import Tree


def insert_trie_into_tree(tree: Tree, trie, parent, letter: str = "root"):
    if trie.word is None:
        tag = letter
    else:
        tag = f"{letter} *"

    tree.create_node(
        identifier=str(id(trie)), tag=tag, parent=str(id(parent)) if parent else None
    )
    for letter, child in trie.children.items():
        insert_trie_into_tree(tree, child, trie, letter)


def visualize_trie(trie):
    tree = Tree()
    insert_trie_into_tree(tree, trie, None)
    print(tree.show(stdout=False))
