def find_zero_index(numbers: list[int], start_index: int, end_index: int) -> int:
    middle_index = (start_index + end_index) // 2

    middle_value = numbers[middle_index]

    if middle_value < 0:
        return find_zero_index(numbers, middle_index + 1, end_index)
    if middle_value > 0:
        return find_zero_index(numbers, start_index, middle_index - 1)
    return middle_index


my_arrays = [
    [-5, -3, -1, -1, -1, -1, -1, 0],
    [-3, -1, -1, -1, -1, -1, 0],
    [-5, -3, -1, -1, -1, -1, 0, 2],
    [-3, -1, -1, -1, -1, 0, 2],
    [-5, -3, -1, -1, -1, 0, 2, 4],
    [-3, -1, -1, -1, 0, 2, 4],
    [-5, -3, -1, -1, 0, 2, 4, 6],
    [-3, -1, -1, 0, 2, 4, 6],
    [-5, -3, -1, 0, 2, 4, 6, 8],
    [-3, -1, 0, 2, 4, 6, 8],
    [-5, -3, 0, 2, 4, 6, 8, 10],
    [-5, -3, 0, 2, 4, 6, 8],
    [-3, 0, 2, 4, 6, 8, 10],
    [-5, 0, 2, 4, 6, 8],
    [0, 2, 4, 6, 8, 10],
    [0, 2, 4, 6, 8],
]

for my_array in my_arrays:
    result = find_zero_index(my_array, 0, len(my_array) - 1)
    assert result == my_array.index(0)


# Complexité:
# si n=2^1-1 = 1
# 1 comparaison
# si n=2^2-1 = 3
# 2 comparaisons
# si n=2^3-1 = 7
# 3 comparaisons
#
# si n=2^x-1
# x comparaisons
# or x = log2(n+1)
#
# complexité O(log(n))
# log(n) est (à peu près) le nombre de chiffres de n écrit en binaire
