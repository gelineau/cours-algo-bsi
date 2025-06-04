from __future__ import annotations
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    salary: float


name = "françois"
age = 56
salary = 14.42
user1 = User(name, age, salary)

user2 = User(name="bob", age=25, salary=12)


def get_minimum_salary(employee1: User, employee2: User) -> float:
    # print(employee1.name)
    return min(employee1.salary, employee2.salary)


def median_user(employee1: User, employee2: User) -> User:
    return User(
        name="median", salary=(employee1.salary + employee2.salary) / 2, age=...
    )


def median_user(employees: list[User]) -> User:
    sum = 0
    nb = 0
    for employee in employees:
        if employee.name != "bob":
            sum += employee.salary
            nb += 1

    return User(name="median", salary=sum / nb, age=0)


print(get_minimum_salary(user1, user2))


@dataclass
class Queue:
    # empty queue : head = tail = None
    head: Node | None
    tail: Node | None


@dataclass
class Node:
    value: int
    previous: Node | None
    next: Node | None


def get_maximum(queue: Queue) -> int:
    # O(n)
    if queue.head == None:
        raise ValueError("queue is empty")

    current = queue.head
    max_value = current.value

    while current.next != None:
        # max_value = max(max_value, current.value)
        if current.value > max_value:
            max_value = current.value
        current = current.next
    return max_value


def remove_first_element(queue: Queue):
    if queue.head == None:
        raise ValueError("empty queue")

    second_element = queue.head.next
    if second_element == None:
        # if queue.head == queue.tail
        queue.head = None
        queue.tail = None
    else:
        queue.head = second_element
        second_element.previous = None
