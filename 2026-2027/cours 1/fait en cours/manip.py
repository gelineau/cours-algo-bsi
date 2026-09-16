def calculate_lengths(words: list[str]) -> list[int]:
    lengths = []
    for word in words:
        length = len(word)
        lengths.append(length)
    return lengths


def calculate_lengths(words: list[str]) -> list[int]:
    return [len(word) for word in words]


def calculate_lengths_and_positions(words: list[str]) -> list[list[int]]:
    result = []
    for i in range(len(words)):
        length = len(words[i])
        result.append([i, length])
    return result


def calculate_lengths_and_positions(words: list[str]) -> list[list[int]]:
    return [[i, len(words[i])] for i in range(len(words))]


words = ["bonjour", "chien", "chat", "oiseau"]
print(calculate_lengths_and_positions(words))


def double_list(numbers: list[int]) -> list[int]:
    result = []
    for number in numbers:
        result.append(number * 2)
    return result


numbers = [5, 7, 9]
print(double_list(numbers))
