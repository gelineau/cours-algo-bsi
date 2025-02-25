from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Stack:
    values: list[int]
    end_index: int


def create_empty_stack() -> Stack:
    return Stack(values=[0] * 10, end_index=-1)


def push_into_stack(value: int, stack: Stack):
    stack.end_index += 1
    if stack.end_index == 10:
        raise IndexError("Stack Overflow")
    stack.values[stack.end_index] = value


def pop_from_stack(stack: Stack) -> int:
    if stack.end_index == -1:
        raise IndexError("empty stack")
    value = stack.values[stack.end_index]
    # not necessary
    stack.values[stack.end_index] = 0

    stack.end_index -= 1
    return value


def evaluate_rpn(expression: str) -> float:
    stack = create_empty_stack()
    words = expression.split()

    for word in words:
        if word == "+":
            operand1 = pop_from_stack(stack)
            operand2 = pop_from_stack(stack)
            value = operand1 + operand2
            push_into_stack(value, stack)
        elif word == "-":
            operand2 = pop_from_stack(stack)
            operand1 = pop_from_stack(stack)
            value = operand1 - operand2
            push_into_stack(value, stack)
        elif word == "*":
            operand1 = pop_from_stack(stack)
            operand2 = pop_from_stack(stack)
            value = operand1 * operand2
            push_into_stack(value, stack)
        elif word == "/":
            operand2 = pop_from_stack(stack)
            operand1 = pop_from_stack(stack)
            value = operand1 / operand2
            push_into_stack(value, stack)
        else:
            value = int(word)
            # value is numeric
            push_into_stack(value, stack)

    final_result = pop_from_stack(stack)
    return final_result


expression = "4 2 + 5 * 6 7 - /"
print(f"{evaluate_rpn(expression)=}")


# @dataclass
# class Queue:
#     values: list[int]
#     head_index: int
#     tail_index: int
#
#
# def create_queue() -> Queue:
#     return Queue(values=[0] * 10, head_index=0, tail_index=-1)
#
#
# def enqueue(value: int, queue: Queue):
#     queue.tail_index += 1
#     queue.values[queue.tail_index] = value
#
#
# def dequeue(queue: Queue) -> int:
#     result = queue.values[queue.head_index]
#     queue.head_index += 1
#     return result
#
# def get_size(queue: Queue)-> int:
#     return queue.tail_index - queue.head_index + 1
#
# def is_empty(queue: Queue) -> bool:
#     return get_size(queue) == 0
#


@dataclass
class Node:
    value: int
    previous: Node | None
    next: Node | None


@dataclass
class Queue:
    head: Node | None
    tail: Node | None


def create_queue() -> Queue: ...
def enqueue(value: int, queue: Queue): ...
def dequeue(queue: Queue) -> int: ...
def get_size(queue: Queue) -> int: ...
def is_empty(queue: Queue) -> bool: ...


queue = create_queue()
enqueue(1, queue)
enqueue(2, queue)
print(dequeue(queue))
enqueue(3, queue)
print(dequeue(queue))
print(dequeue(queue))
