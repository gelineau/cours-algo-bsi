from __future__ import annotations
from dataclasses import dataclass


@dataclass
class MyLinkedList:
    value: int
    next: MyLinkedList | None


node3 = MyLinkedList(value=28, next=None)

node1 = MyLinkedList(value=23, next=MyLinkedList(value=14, next=node3))

print(node1)

print(node1.next)
print(node1.value)

# node1.next = node3

print(node1)


def sum(node: MyLinkedList) -> int:
    sum_of_values = 0
    while node != None:
        sum_of_values += node.value
        node = node.next
    return sum_of_values


def sum(node: MyLinkedList) -> int:
    if node == None:
        return 0

    return node.value + sum(node.next)


print(sum(node1))

print(ord("e"))
