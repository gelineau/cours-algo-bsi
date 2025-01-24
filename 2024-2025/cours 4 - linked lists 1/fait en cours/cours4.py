from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LinkedList:
    value: int
    next: LinkedList | None


#
# a = [1, 2, 3]
# b = a
#
# a[0] = 42
#
# print(a)
#
# print(f"{b=}")
#
# a = 1
# b = a
#
# a = 4
# print(f"{a=} {b=}")
#
# a = "123"
# b = a
#
# a = "456"
# print(f"{a=} {b=}")


list1 = LinkedList(value=12, next=None)
print(list1)

list2 = LinkedList(value=5, next=list1)
print(f"{list2=}")

list1.next = LinkedList(value=14, next=None)
print(f"{list2=}")


my_list = LinkedList(
    value=12, next=LinkedList(value=4, next=LinkedList(value=1, next=None))
)


def get_last_element(linked_list: LinkedList) -> int:
    current_list = linked_list
    while True:
        if current_list.next == None:
            return current_list.value
        current_list = current_list.next


def get_last_element_recursive(linked_list: LinkedList) -> int:
    if linked_list.next == None:
        return linked_list.value

    # list has at least 2 elements
    return get_last_element_recursive(linked_list.next)


print(f"{my_list=}")
print(f"{get_last_element(my_list)=}")
print(f"{get_last_element_recursive(my_list)=}")


def get_nth_element(linked_list: LinkedList, n: int) -> int:
    current_list = linked_list
    for _ in range(n):
        if current_list == None:
            raise IndexError("list is too short")
        current_list = current_list.next

    return current_list.value


def get_nth_element_recursive(linked_list: LinkedList, n: int) -> int:
    if n == 0:
        return linked_list.value

    tail = linked_list.next
    return get_last_element_recursive(tail, n - 1)


print(f"{get_nth_element(my_list, 2)=}")
print(f"{get_nth_element(my_list, 2)=}")


def append(value: int, linked_list: LinkedList):
    new_element = LinkedList(value=value, next=None)
    current_list = linked_list
    while current_list.next != None:
        current_list = current_list.next

    current_list.next = new_element


def append_recursive(value: int, linked_list: LinkedList):
    if linked_list.next == None:
        new_element = LinkedList(value=value, next=None)
        linked_list.next = new_element
    else:
        tail = linked_list.next
        append_recursive(value, tail)


def sum(linked_list: LinkedList) -> int:
    result = 0
    current_list = linked_list
    while current_list != None:
        result += current_list.value
        current_list = current_list.next

    return result


def sum_recursive(linked_list: LinkedList) -> int:
    if linked_list.next == None:
        return linked_list.value

    # at least 2 elements

    return linked_list.value + sum_recursive(linked_list.next)


def find(value: int, linked_list: LinkedList) -> bool:
    current_list = linked_list
    while current_list != None:
        if current_list.value == value:
            return True
        current_list = current_list.next
    return False


def find_recursive(value: int, linked_list: LinkedList) -> bool:
    if value == linked_list.value:
        return True

    if linked_list.next is None:
        return False

    return find_recursive(value, linked_list.next)


def clone(linked_list: LinkedList) -> LinkedList:
    new_list = LinkedList(value=linked_list.value, next=linked_list.next)
    return new_list


cloned = clone(my_list)
print(my_list)
print(cloned)

append(42, my_list)
print(my_list)
print(cloned)
