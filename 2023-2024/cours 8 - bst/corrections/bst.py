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
    new_node = Node(value, left=None, right=None)
    if tree.root is None:
        tree.root = new_node
        return

    current_node = tree.root
    while True:
        if value < current_node.value:
            # insert on left
            if current_node.left is None:
                current_node.left = new_node
                return
            else:
                current_node = current_node.left
        else:
            # insert on right
            if current_node.right is None:
                current_node.right = new_node
                return
            else:
                current_node = current_node.right


data = [8, 10, 3, 1, 6, 14, 13, 7, 4]
bst = create_empty_tree()
for value in data:
    insert(value, bst)
print(bst)


def insert_recursive(value: int, bst: Tree):
    new_node = Node(value, None, None)
    if bst.root is None:
        bst.root = new_node
        return

    insert_into_node(new_node, bst.root)


def insert_into_node(new_node: Node, destination_node: Node):
    if new_node.value < destination_node.value:
        if destination_node.left is None:
            destination_node.left = new_node
        else:
            insert_into_node(new_node, destination_node.left)

    else:
        if destination_node.right is None:
            destination_node.right = new_node
        else:
            insert_into_node(new_node, destination_node.right)


data = [8, 10, 3, 1, 6, 14, 13, 7, 4]
bst = create_empty_tree()
for value in data:
    insert_recursive(value, bst)
pprint(bst)


def display_node_values(node: Node):
    if node.left is not None:
        display_node_values(node.left)
    print(node.value)
    if node.right is not None:
        display_node_values(node.right)


def display_ordered_values(bst: Tree):
    if bst.root is None:
        print("empty tree")
    else:
        display_node_values(bst.root)


display_ordered_values(bst)


def search_in_node(node: Node, value: int) -> bool:
    if value == node.value:
        return True

    if value < node.value:
        if node.left is None:
            return False
        else:
            return search_in_node(node.left, value)

    # value > node.value
    if node.right is None:
        return False
    return search_in_node(node.right, value)


def search_in_tree(tree: Tree, value: int) -> bool:
    if tree.root is None:
        return False

    return search_in_node(tree.root, value)


for i in range(67):
    actual = search_in_tree(bst, i)
    expected = i in data
    assert actual == expected
print("search OK")


def delete_from_node(value: int, node: Node, parent: Node = None):
    if value < node.value:
        if node.left is not None:
            delete_from_node(value, node.left, node)
    elif value > node.value:
        if node.right is not None:
            delete_from_node(value, node.right, node)
    else:  # Found the node to delete
        if node.left is None and node.right is None:  # Case 1: node has no children
            if parent is None:  # Node is the root
                raise NotImplementedError
            elif node == parent.left:
                parent.left = None
            else:
                parent.right = None
        elif node.left is None or node.right is None:  # Case 2: node has one child
            if node.left is None:
                child = node.right
            else:
                child = node.left

            if parent is None:  # Node is the root
                raise NotImplementedError
            elif node == parent.left:
                parent.left = child
            else:
                parent.right = child
        else:  # Case 3: node has two children
            successor = node.right
            while successor.left is not None:  # Find smallest node in the right subtree
                successor = successor.left
            node.value = successor.value
            delete_from_node(successor.value, node.right)


def delete(value: int, bst: Tree):
    if bst.root is None:
        return
    delete_from_node(value, bst.root)


pprint(bst)  # Prints the tree

delete(10, bst)

pprint(bst)  # Prints the updated tree
delete(5, bst)
pprint(bst)
delete(3, bst)
pprint(bst)
