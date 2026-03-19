from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LinkedList:
    value: int
    next: LinkedList | None

    def get_last_element(self) -> int:
        current_element = self
        while current_element.next is not None:
            current_element = current_element.next
        return current_element.value


def get_last_element_rec(linked_list: LinkedList) -> int:
    if linked_list.next is None:
        return linked_list.value

    return get_last_element_rec(linked_list.next)


my_list = LinkedList(value=8, next=None)
print(my_list.get_last_element())
