from __future__ import annotations

from dataclasses import dataclass
import random
import matplotlib.pyplot as plt


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


import time
from collections import deque


def measure_queue_operations(queue_size: int, repetitions: int) -> float:
    """Function to create a queue, initialize it, and measure enqueue and dequeue time"""

    # Create and initialize a queue
    queue = Queue(head=None, tail=None)
    for _ in range(queue_size):
        enqueue(1, queue)

    # Measure the time for k times (append + popleft)
    start_time = time.time()
    for _ in range(repetitions):
        enqueue(2, queue)  # Enqueue
        dequeue(queue)  # Dequeue
    total_time = time.time() - start_time

    return total_time / repetitions


def measure_dequeue_operations(queue_size: int, repetitions: int) -> float:
    """Function to create a queue, initialize it, and measure enqueue and dequeue time"""

    # Create and initialize a deque
    queue = deque([1] * queue_size)

    # Measure the time for k times (append + popleft)
    start_time = time.time()
    for _ in range(repetitions):
        queue.append(queue_size)  # Enqueue
        queue.popleft()  # Dequeue
    total_time = time.time() - start_time

    return total_time / repetitions


def measure_list_operations(queue_size: int, repetitions: int) -> float:
    """Function to create a list, initialize it, and measure enqueue and dequeue time"""

    # Create and initialize a list
    queue = [1] * queue_size

    # Measure the time for k times (append + popleft)
    start_time = time.time()
    for _ in range(repetitions):
        queue.append(queue_size)  # Enqueue
        queue.pop(0)  # Dequeue
    total_time = time.time() - start_time

    return total_time / repetitions


def measure_sort_operations(queue_size: int) -> float:
    """Function to create a list, initialize it, and measure enqueue and dequeue time"""

    # Create and initialize a list
    queue = [random.randrange(100000) for _ in range(queue_size)]

    # Measure the time for k times sort
    start_time = time.time()
    for _ in range(len(queue)):
        queue.insert(0, 0)
    total_time = time.time() - start_time

    return total_time


repetitions = 10

times = []
queue_sizes = [
    1,
    10,
    100,
    1000,
    50_000,
    100_000,
    200_000,
    300_000,
    # 1_000_000,
    # 2_000_000,
    # 4_000_000,
    # 6_000_000,
    # 8_000_000,
    # 10_000_000,
]

for queue_size in queue_sizes:
    # print(f"{queue_size=}")
    # total_time = measure_queue_operations(queue_size, repetitions)
    # print(f"Time for enqueue and dequeue: {total_time} seconds")
    # times.append(total_time)
    #
    # total_time = measure_dequeue_operations(queue_size, repetitions)
    # print(f"Time for enqueue and dequeue from a dequeue: {total_time} seconds")
    # total_time = measure_list_operations(queue_size, repetitions)
    # print(f"Time for enqueue and dequeue from a list: {total_time} seconds")
    #
    total_time = measure_sort_operations(queue_size)
    print(f"Time for sorting: {total_time} seconds")
    times.append(total_time)

# Plotting the results
plt.figure(figsize=(12, 6))

plt.plot(queue_sizes, times)

plt.xlabel("Queue Size")
plt.ylabel("Time (seconds)")
plt.title("Performance of Different Operations")
plt.legend()
plt.grid(True)
plt.show()
