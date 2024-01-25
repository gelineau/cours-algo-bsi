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


def get_element_by_index(numbers: LinkedList, index: int) -> int:
    current_element = numbers
    for _ in range(index):
        try:
            current_element = current_element.next
        except AttributeError:
            raise IndexError("linked list is not long enough")

    return current_element.value


def get_element_by_index_rec(numbers: LinkedList, index: int) -> int:
    if index == 0:
        return numbers.value

    return get_element_by_index(numbers.next, index - 1)


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


print(f"{find_last_element(linked_list)}")
print(f"{get_element_by_index(linked_list, 10)}")
add_element(linked_list, 3)
add_element(linked_list, 31)
add_element(linked_list, 23)
print(f"{linked_list=}")
