from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Element:
    key: str
    value: int


@dataclass
class Dictionary:
    data: list[list[Element]]
    size: int


def calculate_hash(key: str, size: int) -> int:
    return hash(key) % size


def create_empty_dictionary(size: int) -> Dictionary:
    data = []
    for i in range(size):
        data.append([])
    return Dictionary(data=data, size=size)


def insert_into_dictionary(key: str, value: int, dictionary: Dictionary):
    key_hash = calculate_hash(key, dictionary.size)
    for element in dictionary.data[key_hash]:
        if element.key == key:
            element.value = value
            return
    dictionary.data[key_hash].append(Element(key, value))


def get_value(key: str, dictionary: Dictionary):
    key_hash = calculate_hash(key, dictionary.size)
    for element in dictionary.data[key_hash]:
        if element.key == key:
            return element.value
    raise KeyError("key not found")
