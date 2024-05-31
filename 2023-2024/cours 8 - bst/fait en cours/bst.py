from __future__ import annotations
from dataclasses import dataclass
from pprint import pprint


@dataclass
class Node:
    value: int
    left: Node | None
    right: Node | None


@dataclass
class Tree:
    root: Node | None  # None means empty tree


def create_empty_tree() -> Tree:
    return Tree(root=None)


def insert(value: int, tree: Tree):
    new_node = Node(value=value, left=None, right=None)
    if tree.root is None:
        # insert new node into tree
        tree.root = new_node
    else:
        current = tree.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                else:
                    current = current.right


def display_tree_values(tree: Tree):
    if tree.root is None:
        print("empty tree")
    else:
        display_node_values(tree.root)


def display_node_values(node: Node):
    """Recursively display all values, in ascending order"""
    # left subtree
    if node.left is not None:
        display_node_values(node.left)
    # node value
    print(node.value)
    # right subtree
    if node.right is not None:
        display_node_values(node.right)


def search_in_tree(tree: Tree, value: int) -> bool:
    if tree.root is None:
        return False
    return search_in_node(tree.root, value)


def search_in_node(node: Node, value: int) -> bool:
    if value == node.value:
        return True
    if value < node.value:
        if node.left is None:
            return False
        else:
            return search_in_node(node.left, value)
    if value > node.value:
        if node.right is None:
            return False
        else:
            return search_in_node(node.right, value)


tree = create_empty_tree()
data = [8, 10, 3, 1, 6, 14, 13, 7, 4]

for value in data:
    # worst case of tree height:
    # for value in sorted(data):
    insert(value, tree)
pprint(tree)
print(tree)

display_tree_values(tree)
