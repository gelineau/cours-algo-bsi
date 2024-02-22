# from __future__ import annotations
#
# from dataclasses import dataclass
#
#
# @dataclass
# class Stack:
#     values: list[int]
#     end_index: int
#
#
# def create_stack() -> Stack:
#     values = [0] * 10
#     end_index = -1
#     return Stack(values=values, end_index=end_index)
#
#
# def push_into_stack(stack: Stack, value: int):
#     # if stack.end_index == len(stack.values) - 1:
#     #     raise ...
#     try:
#         stack.values[stack.end_index + 1] = value
#     except IndexError:
#         raise IndexError("stack overflow")
#
#     stack.end_index += 1
#
#
# def pop_from_stack(stack: Stack) -> int:
#     if stack.end_index == -1:
#         raise IndexError("Stack is empty")
#     value = stack.values[stack.end_index]
#     # not necessary
#     stack.values[stack.end_index] = 0
#     stack.end_index -= 1
#     return value
#
#
# # stack = create_stack()
# # push_into_stack(stack, 25)
# # push_into_stack(stack, 26)
# # print(f"{pop_from_stack(stack)}")
# # push_into_stack(stack, 27)
# # print(f"{pop_from_stack(stack)}")
# # print(f"{pop_from_stack(stack)}")
# # # print(f"{pop_from_stack(stack)}")
# #
# # for _ in range(11):
# #     push_into_stack(stack, 27)
#
#
# def evaluate_rpn(expression: str) -> float:
#     stack = create_stack()
#
#     for word in expression.split():
#         pass
#


def create_empty_stack() -> list[int]:
    return []


def push_into_stack(stack: list[int], value: int) -> None:
    stack.append(value)


def pop_from_stack(stack: list[int]) -> int:
    return stack.pop()


stack = create_empty_stack()
push_into_stack(stack, 3)
push_into_stack(stack, 2)
print(pop_from_stack(stack))
print(pop_from_stack(stack))


def evaluate_rpn(expression: str) -> float:
    words = expression.split()
    stack = create_empty_stack()
    for word in words:
        if word == "*":
            operand2 = pop_from_stack(stack)
            operand1 = pop_from_stack(stack)
            push_into_stack(stack, operand1 * operand2)
        elif word == "+":
            operand2 = pop_from_stack(stack)
            operand1 = pop_from_stack(stack)
            push_into_stack(stack, operand1 + operand2)
        elif word == "-":
            operand2 = pop_from_stack(stack)
            operand1 = pop_from_stack(stack)
            push_into_stack(stack, operand1 - operand2)
        elif word == "/":
            operand2 = pop_from_stack(stack)
            operand1 = pop_from_stack(stack)
            push_into_stack(stack, operand1 / operand2)
        else:
            push_into_stack(stack, int(word))

    return pop_from_stack(stack)


print(evaluate_rpn("4 2 + 5 * 6 7 - /"))
