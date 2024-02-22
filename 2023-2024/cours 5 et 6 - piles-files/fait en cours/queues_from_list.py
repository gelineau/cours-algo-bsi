from dataclasses import dataclass


@dataclass
class Queue:
    values: list[int]
    first_full_index: int
    first_empty_index: int


def create_queue() -> Queue:
    return Queue(
        values=[0] * 10,
        first_full_index=0,
        first_empty_index=0,
    )


def enqueue(value: int, queue: Queue):
    queue.values[queue.first_empty_index] = value
    queue.first_empty_index += 1


def dequeue(queue: Queue) -> int:
    value = queue.values[queue.first_full_index]
    queue.first_full_index += 1
    return value


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
