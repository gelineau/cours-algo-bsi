from __future__ import annotations

import random


def fusion(data1: list[int], data2: list[int]) -> list[int]:
    result = []
    index1 = 0
    index2 = 0

    while index1 < len(data1) and index2 < len(data2):
        if data1[index1] <= data2[index2]:
            result.append(data1[index1])
            index1 += 1
        else:
            result.append(data2[index2])
            index2 += 1

    while index1 < len(data1):
        result.append(data1[index1])
        index1 += 1

    while index2 < len(data2):
        result.append(data2[index2])
        index2 += 1

    return result


def merge_sort(data: list[int]) -> list[int]:
    if len(data) <= 1:
        return data
    limit = len(data) // 2
    result = fusion(merge_sort(data[:limit]), merge_sort(data[limit:]))
    return result


random.seed(42)
for i in range(1, 100):
    input = [random.randrange(15) for _ in range(i)]
    result = merge_sort(input)
    assert result == sorted(input), f"{input=} {sorted(input)=} {result=}"
print("OK")
