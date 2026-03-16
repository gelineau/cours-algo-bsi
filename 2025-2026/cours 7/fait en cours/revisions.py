# result = []
#
#
# def extract_even(numbers: list[int]) -> list[int]:
#     for number in numbers:
#         if number % 2 == 0:
#             result.append(number)
#
#     return result
#
#
# a = [2, 5, 4, 6]
# print(extract_even(a))
#
# a = [21, 50, 40, 63]
# print(extract_even(a))

#
# a = 5
# FILE_NAME = "/tmp/a"
#
#
# def toto():
#     print(a)
#     a = 8
#     print(a)
#
#
# toto()
# print(a)


# def print_start_of_lines():
#     with open("example.txt") as file:
#         for line in file:
#             # if line[-1] == "\n":
#             #     line = line[:-1]
#             # line = line.replace("\n", "")
#             line = line.rstrip()
#             #
#             # if len(line) < 10:
#             #     line = line + "$" * (10 - len(line))
#
#             line = line + "$" * 10
#             print(line[:10])
#
#
# print_start_of_lines()


def read_first_lines(filename: str, n: int | None = None) -> list[str]:
    with open(filename) as file:
        result = []
        for i, line in enumerate(file):
            if i == 0:
                continue
            if n != None and i >= n:
                break

            result.append(line.rstrip("\n"))
    return result


# read_first_lines("example.txt", 8)


def filter(all_lines: list[str]) -> list[list[str]]:
    for line in all_lines:
        ...
        # .split(",")


all_lines = read_first_lines("example.txt")
filtered_lines = filter(all_lines)
