from __future__ import annotations

import random


def find(sorted_list: list[int], searched_value: int) -> bool:
    min_index = 0
    max_index = len(sorted_list) - 1

    while min_index <= max_index:
        middle_index = (min_index + max_index) // 2
        middle_value = sorted_list[middle_index]

        if middle_value == searched_value:
            return True

        if searched_value > middle_value:
            min_index = middle_index + 1
        elif searched_value < middle_value:
            max_index = middle_index - 1

    return False


data = sorted(random.randrange(1500) for _ in range(10))

for i in range(1500):
    print(i)
    found = find(data, i)
    if i in data:
        assert found
    else:
        assert not found
