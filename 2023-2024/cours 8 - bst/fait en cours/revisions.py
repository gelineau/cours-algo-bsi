from __future__ import annotations
from dataclasses import dataclass

#
# @dataclass
# class User:
#     name: str
#     age: int
#     salary: float
#
#
# user1 = User(name="françois", age=55, salary=3.14)
# user2 = User(name="laurence", age=65, salary=5.14)
#
#
# def get_salary_of_youngest(user1: User, user2: User) -> float:
#     if user1.age < user2.age:
#         return user1.salary
#     return user2.salary
#
#
# def create_median_user(user1: User, user2: User) -> User:
#     return User(name="median", age=(user1.age + user2.age) // 2, salary=0)
#
#
# @dataclass
# class Grade:
#     value: int
#     date: int = 34
#     name: str = ""
#
#
# grade1 = Grade(value=18, date=3, name="yan")
# grade2 = Grade(value=15, name="bob")
#
#
# def set_class_grade(grade1: Grade, grade2: Grade) -> Grade:
#     return Grade(
#         value=grade1.value + grade2.value,
#         date=min(grade1.date, grade2.date),
#         name="aggrégé",
#     )
#
#
# print(set_class_grade(grade1, grade2))


@dataclass
class LinkedList:
    value: int
    next: LinkedList | None


node3 = LinkedList(value=18, next=None)
node2 = LinkedList(value=22, next=node3)
my_list = LinkedList(value=15, next=node2)
print(my_list)


def get_max(linked_list: LinkedList) -> int:
    max_value = 0
    current_node = linked_list
    while current_node != None:
        # max_value = max(max_value, current_node.value)
        if current_node.value > max_value:
            max_value = current_node.value
        current_node = current_node.next

    return max_value


def get_max2(linked_list: LinkedList) -> int:
    if linked_list.next is None:
        return linked_list.value

    return max(linked_list.value, get_max2(linked_list.next))


print(get_max(my_list))
