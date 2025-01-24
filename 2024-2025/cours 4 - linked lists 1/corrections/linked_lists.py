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
print(f"{my_list=}")
print(f"{get_last_element_recursive(my_list)=} {get_last_element(my_list)=}")

#####################
print("*" * 80)


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


print(f"{get_element_by_index(my_list, 1)=} {get_element_by_index_rec(my_list, 2)=}")


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

#####################
print("*" * 80)


def sum_recursive(linked_list: LinkedList) -> int:
    if linked_list.next is None:
        return linked_list.value

    return linked_list.value + sum(linked_list.next)


def sum(linked_list: LinkedList) -> int:
    result = 0
    searched_element = linked_list
    while searched_element is not None:
        result += searched_element.value
        searched_element = searched_element.next

    return result


print(f"{sum(my_list)=} {sum_recursive(my_list)=}")


#####################
print("*" * 80)


def find_recursive(value: int, linked_list: LinkedList) -> bool:
    if value == linked_list.value:
        return True

    if linked_list.next is None:
        return False

    return find_recursive(value, linked_list.next)


def find(value: int, linked_list: LinkedList) -> bool:
    searched_element = linked_list
    while searched_element is not None:
        if searched_element.value == value:
            return True
        searched_element = searched_element.next

    return False


print(f"{find(6, my_list)=} {find_recursive(6, my_list)=}")
print(f"{find(8, my_list)=} {find_recursive(8, my_list)=}")

#####################
print("*" * 80)


def replace(value1: int, value2: int, linked_list: LinkedList):
    searched_element = linked_list
    while searched_element is not None:
        if searched_element.value == value1:
            searched_element.value = value2
        searched_element = searched_element.next


def replace_recursive(value1: int, value2: int, linked_list: LinkedList):
    if linked_list.value == value1:
        linked_list.value = value2
    if linked_list.next is None:
        return
    replace_recursive(value1, value2, linked_list.next)


print(f"{my_list=}")
replace(1, 42, my_list)
print(f"{my_list=}")
replace_recursive(42, 99, my_list)
print(f"{my_list=}")

#####################
print("*" * 80)


def clone(linked_list: LinkedList) -> LinkedList:
    result = LinkedList(value=linked_list.value, next=None)
    end_value = result

    searched_element = linked_list.next
    while searched_element is not None:
        end_value.next = LinkedList(value=searched_element.value, next=None)
        searched_element = searched_element.next
        end_value = end_value.next

    return result


def clone_recursive(linked_list: LinkedList) -> LinkedList:
    result = LinkedList(value=linked_list.value, next=None)
    if linked_list.next is not None:
        result.next = clone_recursive(linked_list.next)

    return result


my_new_list = clone_recursive(my_list)
print(f"{my_new_list=}")
replace(99, 88, my_new_list)
print(f"{my_list=}")
print(f"{my_new_list=}")

#####################
print("*" * 80)


def remove_recursive(value: int, linked_list: LinkedList) -> LinkedList | None:
    if linked_list.value == value:
        if linked_list.next is None:
            return None
        return remove_recursive(value, linked_list.next)

    if linked_list.next is None:
        return LinkedList(linked_list.value, None)
    return LinkedList(linked_list.value, remove_recursive(value, linked_list.next))


print(f"{my_list=}")
list_with_99_removed = remove_recursive(99, my_list)
print(f"{list_with_99_removed=}")

#####################
print("*" * 80)


def linked_list_to_string(linked_list: LinkedList) -> str:
    elements = []
    current_element = linked_list
    while current_element is not None:
        elements.append(str(current_element.value))
        current_element = current_element.next
    return " -> ".join(elements)


def linked_list_to_string_recursive(linked_list: LinkedList) -> str:
    if linked_list.next is None:
        return str(linked_list.value)
    return (
        str(linked_list.value)
        + " -> "
        + linked_list_to_string_recursive(linked_list.next)
    )


print(f"{linked_list_to_string(my_list)=}")
print(f"{linked_list_to_string_recursive(my_list)=}")


#####################
print("*" * 80)


def extend(list1: LinkedList, list2: LinkedList):
    # Find the last element of the first list
    current_element = list1
    while current_element.next is not None:
        current_element = current_element.next

    # Link the last element of the first list to the second list
    current_element.next = list2


def extend_recursive(list1: LinkedList, list2: LinkedList):
    # If we reach the last element of the first list, link it to the second list
    if list1.next is None:
        list1.next = list2
    else:
        # Recur for the next element
        extend_recursive(list1.next, list2)


list_a = LinkedList(1, LinkedList(2, LinkedList(3, None)))
extend(my_list, list_a)
print(f"{linked_list_to_string(my_list)=}")

list_b = LinkedList(9, LinkedList(8, LinkedList(7, None)))
extend_recursive(my_list, list_b)
print(f"{linked_list_to_string(my_list)=}")

#####################
print("*" * 80)


def get_size(linked_list: LinkedList) -> int:
    count = 0
    current_element = linked_list
    while current_element is not None:
        count += 1
        current_element = current_element.next
    return count


def get_size_recursive(linked_list: LinkedList) -> int:
    if linked_list.next is None:
        return 1
    return 1 + get_size_recursive(linked_list.next)


print(f"{get_size(my_list)=}")
print(f"{get_size_recursive(my_list)=}")


#####################
print("*" * 80)


def extract_sublist(linked_list: LinkedList, n: int) -> LinkedList | None:
    current_element = linked_list

    # Traverse the list until the n-th element
    for _ in range(n):
        current_element = current_element.next

    # Return the rest of the list starting from the n-th element
    return current_element


print(f"{extract_sublist(my_list, 5)=}")
