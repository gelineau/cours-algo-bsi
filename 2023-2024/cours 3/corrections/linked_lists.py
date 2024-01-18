from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass


# déclaration du modèle et de ses attributs
@dataclass
class LinkedList:
    value: int
    next: LinkedList | None


# création d'un objet
linked_list = LinkedList(value=12, next=None)

# accès à un attribut
linked_list.value = 13

####################
print("*" * 80)

a = [1, 2, 3]
b = a

a[0] = 42
print(f"{a=}")
print(f"{b=}")

print()
b = deepcopy(a)
a[0] = 15
print(f"{a=}")
print(f"{b=}")

####################
print("*" * 80)

linked_list = LinkedList(5, None)

print(f"{linked_list=}")
linked_list.value = 4
print(f"{linked_list=}")

linked_list2 = linked_list
linked_list2.value = 7

print(f"{linked_list2=} {linked_list=}")

linked_list2 = deepcopy(linked_list)
linked_list2.value = 9
print(f"{linked_list2=} {linked_list=}")

linked_list2.next = linked_list
print(f"{linked_list2=}")


####################
print("*" * 80)


def get_last_element(linked_list: LinkedList) -> int:
    searched_item = linked_list
    while True:
        if searched_item.next == None:
            return searched_item.value
        searched_item = searched_item.next


def get_last_element_recursive(linked_list: LinkedList) -> int:
    if linked_list.next is None:
        return linked_list.value
    return get_last_element_recursive(linked_list.next)


my_list = LinkedList(1, LinkedList(2, LinkedList(3, None)))
print(f"{get_last_element_recursive(my_list)=} {get_last_element(my_list)=}")

#####################
print("*" * 80)


def append(value: int, linked_list: LinkedList):
    new_element = LinkedList(value, None)

    # Traverse the linked list to find the last element
    current_element = linked_list
    while current_element.next is not None:
        current_element = current_element.next

    # Append the new element to the end of the linked list
    current_element.next = new_element


def append_recursive(value: int, linked_list: LinkedList):
    if linked_list.next is None:
        new_element = LinkedList(value=value, next=None)
        linked_list.next = new_element
    else:
        append_recursive(value, linked_list.next)


my_list = LinkedList(1, next=None)
for i in range(8):
    append(i, my_list)
print(my_list)

my_list = LinkedList(1, next=None)
for i in range(8):
    append_recursive(i, my_list)
print(my_list)
