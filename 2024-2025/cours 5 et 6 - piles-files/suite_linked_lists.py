from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass


# déclaration du modèle et de ses attributs
@dataclass
class LinkedList:
    value: int
    next: LinkedList | None


#####################
print("*" * 80)


def append_recursive(value: int, linked_list: LinkedList):
    if linked_list.next is None:
        new_element = LinkedList(value=value, next=None)
        linked_list.next = new_element
    else:
        append_recursive(value, linked_list.next)


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

    return find(value, linked_list.next)


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


def remove(value: int, linked_list: LinkedList) -> LinkedList | None:
    # Handle the case where the first node needs to be removed
    while linked_list is not None and linked_list.value == value:
        linked_list = linked_list.next

    current = linked_list

    while current is not None and current.next is not None:
        if current.next.value == value:
            current.next = current.next.next  # Skip the node with the specified value
        else:
            current = current.next

    return linked_list  # Return the modified linked list


append_recursive(99, my_list)
append_recursive(42, my_list)
append_recursive(99, my_list)
my_new_list = clone(my_list)

print(f"{my_list=}")
list_with_99_removed = remove_recursive(99, my_list)
print(f"{list_with_99_removed=}")

print(f"{my_new_list=}")
list_with_99_removed = remove(99, my_new_list)
print(f"{list_with_99_removed=}")


#####################
print("*" * 80)


def remove_first(linked_list: LinkedList) -> LinkedList | None:
    return linked_list.next


my_list_without_first_element = remove_first(my_list)

print(f"{my_list=}")
print(f"{my_list_without_first_element=}")


#####################
print("*" * 80)


def add_first(value: int, linked_list: LinkedList) -> LinkedList:
    new_node = LinkedList(value, linked_list)
    return new_node


my_list_with_first_element = add_first(11, my_list)

print(f"{my_list=}")
print(f"{my_list_with_first_element=}")


#####################
print("*" * 80)


def to_list(linked_list: LinkedList) -> list[int]:
    values = []
    current = linked_list

    while current is not None:
        values.append(current.value)
        current = current.next

    return values


def to_list_recursive(linked_list: LinkedList) -> list[int]:
    if linked_list.next is None:
        return [linked_list.value]

    return [linked_list.value] + to_list_recursive(linked_list.next)


# Convert the linked list to a Python list
normal_list = to_list(my_list)
# Print the result
print(f"{normal_list=}")

# Convert the linked list to a Python list
normal_list = to_list_recursive(my_list)
# Print the result
print(f"{normal_list=}")

#####################
print("*" * 80)


def extend_list(list1: LinkedList, list2: LinkedList):
    current = list1
    while current.next is not None:
        current = current.next

    current.next = list2


def extend_list_recursive(list1: LinkedList, list2: LinkedList):
    if list1.next is None:
        list1.next = list2
    else:
        extend_list(list1.next, list2)


list1 = LinkedList(1, LinkedList(2, None))
list2 = LinkedList(3, LinkedList(4, None))

extend_list(list1, list2)
print(f"{list1=}")

list1 = LinkedList(1, LinkedList(2, None))
list2 = LinkedList(3, LinkedList(4, None))

extend_list(list1, list2)
print(f"{list1=}")


#####################
print("*" * 80)


def list_length(linked_list: LinkedList) -> int:
    length = 0
    current = linked_list

    while current is not None:
        length += 1
        current = current.next

    return length


def list_length_recursive(linked_list: LinkedList) -> int:
    if linked_list.next is None:
        return 1

    return 1 + list_length_recursive(linked_list.next)


print(f"{list_length(list1)=}")
print(f"{list_length_recursive(list1)=}")


#####################
print("*" * 80)


def extract_sublist_from_nth(n: int, linked_list: LinkedList) -> LinkedList:
    current = linked_list

    # Move to the nth element (starting with 0)
    for count in range(n):
        current = current.next

    # Return the sublist starting from the nth element
    return current


def extract_sublist_from_nth_recursive(n: int, linked_list: LinkedList) -> LinkedList:
    if n == 0:
        return linked_list

    return extract_sublist_from_nth_recursive(n - 1, linked_list.next)


print(f"{extract_sublist_from_nth(2, list1)=}")
print(f"{extract_sublist_from_nth_recursive(2, list1)=}")


#####################
print("*" * 80)


@dataclass
class Node:
    value: int
    previous: Node | None
    next: Node | None


@dataclass
class Queue:
    """
    if head is None and tail is None, the queue is empty
    """

    head: Node | None
    tail: Node | None


def dequeue(queue: Queue) -> int:
    if queue.head is None:
        raise Exception("queue is empty")
    value = queue.head.value
    if queue.head == queue.tail:
        queue.head = queue.tail = None
    else:
        queue.head = queue.head.next
        queue.head.previous = None
    return value


def enqueue(data: int, queue: Queue):
    new_node = Node(data, None, None)
    if queue.tail is None:
        queue.head = queue.tail = new_node
        return
    queue.tail.next = new_node
    new_node.previous = queue.tail
    queue.tail = new_node


queue = Queue(head=None, tail=None)
enqueue(1, queue)
enqueue(2, queue)
print(dequeue(queue))
enqueue(3, queue)
enqueue(4, queue)
print(dequeue(queue))
print(dequeue(queue))
print(dequeue(queue))
enqueue(5, queue)
enqueue(6, queue)
print(dequeue(queue))
enqueue(7, queue)
enqueue(8, queue)
print(dequeue(queue))
print(dequeue(queue))
print(dequeue(queue))
enqueue(9, queue)
enqueue(10, queue)
enqueue(11, queue)
print(dequeue(queue))
print(dequeue(queue))
print(dequeue(queue))

# queue is empty
print(dequeue(queue))
