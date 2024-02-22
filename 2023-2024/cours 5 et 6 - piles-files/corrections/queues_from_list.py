from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Queue:
    values: list[int]
    head_index: int
    tail_index: int


def create_queue() -> Queue:
    return Queue([0] * 10, head_index=0, tail_index=-1)


def enqueue(value: int, queue: Queue):
    if queue.tail_index == 9:
        raise Exception("Queue is full")

    queue.tail_index += 1
    queue.values[queue.tail_index] = value


def dequeue(queue: Queue) -> int:
    result = queue.values[queue.head_index]
    queue.head_index += 1
    return result


def is_empty(queue: Queue) -> bool:
    return queue.head_index == queue.tail_index


def get_size(queue: Queue) -> int:
    return queue.tail_index - queue.head_index + 1


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
# enqueue(10, queue)
# enqueue(11, queue)
