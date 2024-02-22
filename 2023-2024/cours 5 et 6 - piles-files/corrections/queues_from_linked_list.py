from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    value: int
    previous: Node | None
    next: Node | None


@dataclass
class Queue:
    """
    if head is None and tail is None,
    the queue is empty
    """

    head: Node | None
    tail: Node | None


def dequeue(queue: Queue) -> int:
    if queue.head is None:
        raise Exception("queue is empty")
    value = queue.head.value
    if queue.head == queue.tail:
        queue.head = queue.tail = None
    else:
        queue.head = queue.head.next
        queue.head.previous = None
    return value


def enqueue(data: int, queue: Queue):
    new_node = Node(data, None, None)
    if queue.tail is None:
        queue.head = queue.tail = new_node
        return
    queue.tail.next = new_node
    new_node.previous = queue.tail
    queue.tail = new_node


queue = Queue(head=None, tail=None)
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
enqueue(10, queue)
enqueue(11, queue)
print(dequeue(queue))
print(dequeue(queue))
print(dequeue(queue))
#
# # queue is empty
# print(dequeue(queue))
