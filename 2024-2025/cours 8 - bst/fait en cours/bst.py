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
    root: Node | None


def create_empty_tree() -> Tree:
    return Tree(root=None)


def insert(value: int, tree: Tree):
    new_node = Node(value=value, left=None, right=None)

    if tree.root == None:
        tree.root = new_node
        return

    current_node = tree.root
    while True:
        if value < current_node.value:
            # insert on left
            if current_node.left == None:
                current_node.left = new_node
                return
            current_node = current_node.left

        else:
            # insert on right
            if current_node.right == None:
                current_node.right = new_node
                return
            current_node = current_node.right


def insert_recursive(value: int, tree: Tree):
    new_node = Node(value=value, left=None, right=None)

    if tree.root == None:
        tree.root = new_node
        return

    insert_into_node(new_node, tree.root)


def insert_into_node(new_node: Node, destination_node: Node):
    if new_node.value < destination_node.value:
        if destination_node.left == None:
            destination_node.left = new_node
        else:
            insert_into_node(new_node, destination_node.left)

    else:
        if destination_node.right == None:
            destination_node.right = new_node
        else:
            insert_into_node(new_node, destination_node.right)


def display_recursive(tree: Tree):
    if tree.root == None:
        print("arbre vide")
        return

    display_from_node(tree.root)


def display_from_node(node: Node):
    # afficher tout node.left
    if node.left != None:
        display_from_node(node.left)

    print(node.value)

    # afficher tout node.right
    if node.right != None:
        display_from_node(node.right)


data = [8, 10, 3, 1, 6, 14, 13, 7, 4]
tree = create_empty_tree()
for number in data:
    insert_recursive(number, tree)

display_recursive(tree)
