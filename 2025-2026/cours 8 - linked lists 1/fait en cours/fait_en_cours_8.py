from __future__ import annotations
from dataclasses import dataclass


@dataclass
class LinkedList:
    value: int
    next: LinkedList | None

    def append(self: LinkedList, value: int):
        current = self
        while current.next is not None:
            current = current.next
        current.next = LinkedList(value=value, next=None)

    def append_rec(self: LinkedList, value: int):
        if self.next is None:
            self.next = LinkedList(value=value, next=None)
        else:
            self.next.append_rec(value)


#
#
# my_list = LinkedList(value=12, next=None)
# # my_list = LinkedList(12, None)
# my_list2 = LinkedList(value=12, next=None)
#
# print(f"ma liste est : {my_list=}")
# print(f"ma liste est : {my_list2=}")
#
# my_list.value = 1
#
# print(f"ma liste est : {my_list=}")
# print(f"ma liste est : {my_list2=}")
#
# print(f"{my_list.value}")
#
# a = my_list.value
#
# my_list2.value = my_list.value
#
#
# list1 = LinkedList(value=12, next=None)
#
# list2 = LinkedList(value=27, next=list1)
#
# print(f"{list2=}")
#
# list3 = LinkedList(value=42, next=list2)
# print(f"{list3=}")


def get_last_value(linked_list: LinkedList) -> int:
    current = linked_list
    while current.next is not None:
        current = current.next
    return current.value


def get_last_value_rec(linked_list: LinkedList) -> int:
    if linked_list.next is None:
        return linked_list.value

    return get_last_value(linked_list.next)


def append(linked_list: LinkedList, value: int):
    current = linked_list
    while current.next is not None:
        current = current.next

    current.next = LinkedList(value=value, next=None)


my_list = LinkedList(
    value=12, next=LinkedList(value=4, next=LinkedList(value=1, next=None))
)
print(my_list)
# print(f"  {get_last_value(my_list)=}")
my_list.append(34)
print(my_list)
