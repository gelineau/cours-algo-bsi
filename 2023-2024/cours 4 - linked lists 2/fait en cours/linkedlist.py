from __future__ import annotations
from dataclasses import dataclass


@dataclass
class LinkedList:
    value: int
    next: LinkedList | None


# créer une instance
linked_list = LinkedList(value=5, next=None)


# accéder à un attribut

linked_list.value = 9
print(f"{linked_list.value}")
print(f"{linked_list=}")

linked_list2 = LinkedList(value=3, next=None)
print(f"{linked_list2=}")

linked_list3 = LinkedList(value=1, next=linked_list2)
print(f"{linked_list3}")


linked_list = LinkedList(
    value=2, next=LinkedList(value=3, next=LinkedList(value=5, next=None))
)


def find_last_element(numbers: LinkedList) -> int:
    current_element = numbers
    while True:
        if current_element.next is None:
            return current_element.value
        current_element = current_element.next


def find_last_element_recursive(numbers: LinkedList) -> int:
    if numbers.next is None:
        return numbers.value

    return find_last_element(numbers.next)


def add_element(numbers: LinkedList, new_value: int):
    current_element = numbers
    while current_element.next != None:
        current_element = current_element.next

    current_element.next = LinkedList(value=new_value, next=None)


def add_element_rec(numbers: LinkedList, new_value: int):
    if numbers.next is None:
        numbers.next = LinkedList(value=new_value, next=None)
    else:
        add_element_rec(numbers.next, new_value)


add_element(linked_list, 3)
add_element(linked_list, 31)
add_element(linked_list, 23)
print(f"{linked_list=}")


def remove_first(numbers: LinkedList) -> LinkedList:
    return numbers.next


def add_first(numbers: LinkedList, value: int) -> LinkedList:
    new_numbers = LinkedList(value=value, next=numbers)
    return new_numbers


def calculate_sum(numbers: LinkedList) -> int:
    total = 0
    current = numbers
    while current is not None:
        total += current.value
        current = current.next
    return total


def calculate_sum_recursive(numbers: LinkedList) -> int:
    if numbers.next is None:
        return numbers.value
    return numbers.value + calculate_sum_recursive(numbers.next)


def calculate_sum_recursive(numbers: LinkedList | None) -> int:
    if numbers is None:
        return 0
    return numbers.value + calculate_sum_recursive(numbers.next)


def is_in_list(value: int, numbers: LinkedList) -> bool:
    current = numbers
    while current is not None:
        if current.value == value:
            return True
        current = current.next
    return False


def is_in_list_rec(value: int, numbers: LinkedList) -> bool:
    if numbers.next is None:
        return numbers.value == value

    tail = numbers.next

    return numbers.value == value or is_in_list_rec(value, tail)


def is_in_list_rec(value: int, numbers: LinkedList | None) -> bool:
    if numbers is None:
        return False

    tail = numbers.next

    return numbers.value == value or is_in_list_rec(value, tail)
