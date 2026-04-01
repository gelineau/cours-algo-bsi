from __future__ import annotations

from dataclasses import dataclass
from pprint import pprint
from zipfile import sizeEndCentDir


@dataclass
class Element:
    key: str
    value: int


@dataclass
class Dictionary:
    size: int
    data: list[list[Element]]


def calculate_hash(key: str, size: int) -> int:
    # return hash between 0 and size - 1
    return hash(key) % size


def create_empty_dictionary(size: int) -> Dictionary:
    data = []
    for i in range(size):
        data.append([])
    return Dictionary(size=size, data=data)


print(create_empty_dictionary(10))


def insert_into_dictionary(key: str, value: int, dictionary: Dictionary):
    key_hash = calculate_hash(key, dictionary.size)
    elements = dictionary.data[key_hash]

    for element in elements:
        if element.key == key:
            element.value = value
            return

    elements.append(Element(key=key, value=value))


def get_from_dictionary(key: str, dictionary: Dictionary) -> int:
    key_hash = calculate_hash(key, dictionary.size)
    elements = dictionary.data[key_hash]

    for element in elements:
        if element.key == key:
            return element.value

    raise KeyError(f"key {key} not found")


my_dict = create_empty_dictionary(10)
insert_into_dictionary("chat", 1, my_dict)
insert_into_dictionary("chien", 2, my_dict)
insert_into_dictionary("oiseau", 3, my_dict)
insert_into_dictionary("chat", 100, my_dict)


print(get_from_dictionary("chattttt", my_dict))
