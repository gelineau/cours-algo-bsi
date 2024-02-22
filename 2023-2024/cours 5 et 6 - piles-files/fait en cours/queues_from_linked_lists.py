from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Queue:
    head: Node | None
    tail: Node | None


@dataclass
class Node:
    value: int
    previous: Node | None
    next: Node | None


def create_queue() -> Queue:
    return Queue(None, None)


# O(1)
def dequeue(queue: Queue) -> int:
    if queue.head == queue.tail:
        value = queue.head.value
        queue.head = None
        queue.tail = None
    else:
        value = queue.head.value
        new_head = queue.head.next
        new_head.previous = None
        queue.head = new_head
        return value


# O(1)
def enqueue(value: int, queue: Queue):
    new_node = Node(value=value, previous=None, next=None)
    if queue.head is None and queue.tail is None:
        queue.head = new_node
        queue.tail = new_node
    else:
        queue.tail.next = new_node
        new_node.previous = queue.tail
        queue.tail = new_node


queue = create_queue()

enqueue(1, queue)
enqueue(2, queue)
print(dequeue(queue))
enqueue(3, queue)
enqueue(4, queue)
print(dequeue(queue))
print(dequeue(queue))
print(dequeue(queue))
enqueue(5, queue)
enqueue(6, queue)
print(dequeue(queue))
enqueue(7, queue)
enqueue(8, queue)
print(dequeue(queue))
print(dequeue(queue))
print(dequeue(queue))
enqueue(9, queue)
