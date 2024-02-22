from __future__ import annotations

from dataclasses import dataclass

# solution with just a list:
#
# def create_stack() -> list[int]:
#     return []
#
#
# def push_into_stack(value: int, stack: list[int]):
#     stack.append(value)
#
#
# def pop_from_stack(stack: list[int]) -> int:
#     return stack.pop()


# solution with a list of 10 elements and an index


@dataclass
class Stack:
    values: list[int]
    end_index: int


def create_stack() -> Stack:
    return Stack([0] * 10, -1)


def push_into_stack(value: int, stack: Stack):
    stack.end_index += 1
    # TODO manage stack overflow
    stack.values[stack.end_index] = value


def pop_from_stack(stack: Stack) -> int:
    # TODO manage empty stack
    value = stack.values[stack.end_index]

    # not necessary
    stack.values[stack.end_index] = 0

    stack.end_index -= 1
    return value


# my_stack = create_stack()
# pop_from_stack(my_stack)
# push_into_stack(my_stack, 1)
# push_into_stack(my_stack, 2)
# push_into_stack(my_stack, 3)
# for _ in range(10):
#     push_into_stack(my_stack, 3)
#
#
# element = pop_from_stack(my_stack)
# print(element)
# element = pop_from_stack(my_stack)
# print(element)
#
# push_into_stack(my_stack, 42)
# print(my_stack)


def evaluate_rpn(expression: str) -> int:
    """
    e.g. expression = "4 2 + 5 * 6 7 - /"
    means (4+2)*5 / (6-7)

    """
    stack = create_stack()

    words = expression.split()
    for word in words:
        if word == "+":
            # first operand is popped second
            operand2 = pop_from_stack(stack)
            operand1 = pop_from_stack(stack)
            result = operand1 + operand2
            push_into_stack(result, stack)
        elif word == "-":
            operand2 = pop_from_stack(stack)
            operand1 = pop_from_stack(stack)
            result = operand1 - operand2
            push_into_stack(result, stack)
        elif word == "*":
            operand2 = pop_from_stack(stack)
            operand1 = pop_from_stack(stack)
            result = operand1 * operand2
            push_into_stack(result, stack)
        elif word == "/":
            operand2 = pop_from_stack(stack)
            operand1 = pop_from_stack(stack)
            result = operand1 // operand2
            push_into_stack(result, stack)
        else:  # word is a number
            word_as_int = int(word)
            push_into_stack(word_as_int, stack)

    return pop_from_stack(stack)


print(evaluate_rpn("4 2 + 5 * 6 7 - /"))
