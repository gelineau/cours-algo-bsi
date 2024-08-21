# from __future__ import annotations


def find(numbers: list[int], searched_value: int) -> bool:
    for index in range(len(numbers)):
        number = numbers[index]
        if number == searched_value:
            return True
    return False


def find2(numbers: list[int], searched_value: int) -> bool:
    for number in numbers:
        if number == searched_value:
            return True
    return False


def find_position(numbers: list[int], searched_value: int) -> int | None:
    for index in range(len(numbers)):
        number = numbers[index]
        if number == searched_value:
            return index
    return None


numbers = [2, 5, 1, 3, 6]

print(
    f"{find(numbers, 1)=} {find2(numbers, 1)=} {find_position(numbers, 1)=} {find_position(numbers, 42)=}"
)
