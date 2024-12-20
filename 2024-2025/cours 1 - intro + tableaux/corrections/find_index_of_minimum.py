from __future__ import annotations

import random


def find_index_of_minimum(data: list[int], start_index: int) -> int:
    value_minimum = data[start_index]
    index_minimum = start_index
    for index_to_compare in range(start_index + 1, len(data)):
        if data[index_to_compare] < value_minimum:
            value_minimum = data[index_to_compare]
            index_minimum = index_to_compare
    return index_minimum


random.seed(42)
for _ in range(1000):
    input = [random.randrange(15) for _ in range(15)]
    index_of_minimum = find_index_of_minimum(input, 3)
    assert min(input[3:]) == input[index_of_minimum]
print("OK")
