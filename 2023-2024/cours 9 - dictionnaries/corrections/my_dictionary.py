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


def create_empty_dictionary(size: int) -> Dictionary:
    values = []
    for _ in range(size):
        values.append([])

    return Dictionary(data=values, size=size)


def display_dictionary(dictionary: Dictionary):
    print("{", end="")
    for element_list in dictionary.data:
        for element in element_list:
            print(f"{element.key}:{element.value}", end=",")
    print("}")


def calculate_hash(key: str, size: int) -> int:
    return hash(key) % size


def insert_into_dictionary(key: str, value: int, dictionary: Dictionary):
    key_hash = calculate_hash(key, dictionary.size)
    for element in dictionary.data[key_hash]:
        if element.key == key:
            element.value = value
            return
    dictionary.data[key_hash].append(Element(key, value))


def get_value(key: str, dictionary: Dictionary) -> int:
    key_hash = calculate_hash(key, dictionary.size)
    for element in dictionary.data[key_hash]:
        if element.key == key:
            return element.value
    raise KeyError("Not found")


if __name__ == "__main__":
    # create an empty dictionary
    frequency = create_empty_dictionary(4)

    # add elements

    for word, number in (("a", 1), ("b", 2), ("c", 3), ("d", 4), ("e", 5)):
        insert_into_dictionary(word, number, frequency)

    print(frequency)
    display_dictionary(frequency)

    # update a value (no duplicated keys)
    insert_into_dictionary("a", 42, frequency)

    display_dictionary(frequency)

    # search a value

    print("value for 'a': ", get_value("a", frequency))
    print(get_value("dud", frequency))
