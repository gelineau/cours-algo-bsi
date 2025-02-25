from __future__ import annotations
from dataclasses import dataclass
from inspect import stack


#
# @dataclass
# class LinkedList:
#     value: int
#     next: LinkedList | None
#
#
# def get_nth_element(linked_list: LinkedList, n: int) -> int:
#     current_element = linked_list
#     for _ in range(n):
#         current_element = current_element.next
#     return current_element.value
#
#
# def get_length(linked_list: LinkedList) -> int:
#     current_element = linked_list
#     result = 0
#     while current_element != None:
#         current_element = current_element.next
#         result += 1
#     return result
#
#
# def delete_last_element(linked_list: LinkedList):
#     current_element = linked_list
#     try:
#         while current_element.next.next != None:
#             current_element = current_element.next
#     except AttributeError:
#         raise IndexError("delete is not implemented for short lists ")
#     current_element.next = None
#
#
# def add_on_start(value: int, linked_list: LinkedList) -> LinkedList:
#     new_element = LinkedList(value=value, next=linked_list)
#     return new_element
#
#
# def delete_first_element(linked_list: LinkedList) -> LinkedList:
#     return linked_list.next
#
#
# my_list = LinkedList(
#     value=1, next=LinkedList(value=2, next=LinkedList(value=3, next=None))
# )
# print(f"{my_list=}")
# print(f"{get_length(my_list)=}")
#
# # delete_last_element(my_list)
# # print(f"{my_list=}")
# # delete_last_element(my_list)
# # delete_last_element(my_list)
#
# my_list = delete_first_element(my_list)
# print(f"{my_list=}")
#
#
# a = [3, 1, 6, 42, 8, 12]
#
#
# def find(value: int, numbers: list[int]) -> bool:
#     """
#     O(n)
#     """
#     for number in numbers:
#         if number == value:
#             return True
#     return False

#
# def create_empty_stack() -> list[int]:
#     """
#     O(1)
#     """
#     return []
#
#
# def push_into_stack(value: int, stack: list[int]):
#     """
#     O(1)
#     """
#     stack.append(value)
#
#
# def pop_from_stack(stack: list[int]) -> int:
#     """
#     O(1)
#     """
#     return stack.pop()
#
#
# stack = create_empty_stack()
# push_into_stack(1, stack)
# push_into_stack(2, stack)
# push_into_stack(3, stack)
# print(pop_from_stack(stack))
# push_into_stack(4, stack)
# print(pop_from_stack(stack))
# print(pop_from_stack(stack))
# print(pop_from_stack(stack))


# dataclass Stack
# attributs :
# tableau de 10 éléments
# indice du dernier élément utilisé
@dataclass
class Stack:
    values: list[int]
    end_index: int


def create_empty_stack() -> Stack:
    """
    O(1)
    """
    stack = Stack(values=[0] * 10, end_index=-1)
    return stack


def push_into_stack(value: int, stack: Stack):
    stack.values[stack.end_index + 1] = value
    stack.end_index += 1


def pop_from_stack(stack: Stack) -> int:
    if stack.end_index == -1:  # empty stack
        raise IndexError("popping from empty stack")
    value = stack.values[stack.end_index]
    stack.values[stack.end_index] = 0  # not necessary
    stack.end_index -= 1
    return value


stack = create_empty_stack()
# print(stack)
# push_into_stack(1, stack)
# push_into_stack(2, stack)
# push_into_stack(3, stack)
# print(pop_from_stack(stack))
# push_into_stack(4, stack)
# print(pop_from_stack(stack))
# print(pop_from_stack(stack))
# print(pop_from_stack(stack))


# print(pop_from_stack(stack))


expression = "4 2 + 5 * 6 7 - /"
# 4 2 + 5 * 6 7 - /
# 6     5 * 6 7 - /
# 30        6 7 - /
# 30          -1   /
# -30

print(expression.split())
# stack = create_empty_stack()
# for word in expression.split():
#     if "+"  pop pop  +  push
#     if "-"
#     if "*"
#     if "/"
#     else number = int(word)
