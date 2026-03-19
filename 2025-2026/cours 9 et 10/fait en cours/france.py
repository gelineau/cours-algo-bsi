from collections import Counter


def read_words_from_file() -> list[str]:
    with open("france.txt", encoding="utf-8") as file:
        words = []
        for line in file:
            words_in_line = line.split()
            words.extend(words_in_line)
    return words


def read_words_from_file2() -> list[str]:
    with open("france.txt", encoding="utf-8") as file:
        content = file.read()

    return content.split()


def get_most_frequent_word1(words: list[str]) -> str:
    # O(n2)
    most_frequent_word = None
    max_frequency = 0

    for word1 in words:
        count = 0
        for word2 in words:
            if word1 == word2:
                count += 1
        # word1 is present count times
        if count > max_frequency:
            max_frequency = count
            most_frequent_word = word1

    return most_frequent_word


def get_most_frequent_word2(words: list[str]) -> str:
    # words.sort()
    sorted_words = sorted(words)

    most_frequent_word = None
    max_occurences = 0

    current_word = None
    current_occurence_number = 0

    for word in words:
        if word == current_word:
            current_occurence_number += 1
        else:
            if current_occurence_number > max_occurences:
                max_occurences = current_occurence_number
                most_frequent_word = current_word
            current_word = word
            current_occurence_number = 1
    return most_frequent_word


words = read_words_from_file2()


def get_most_frequent_word3(words: list[str]) -> str:
    occurences = {}  # key: word, value: nb of occurences
    for word in words:
        if word in occurences:
            occurences[word] += 1
        else:
            occurences[word] = 1
    print(occurences)

    maximum = 0
    word_maximum = None
    for word, occurence_nb in occurences.items():
        if occurence_nb > maximum:
            maximum = occurence_nb
            word_maximum = word

    # for word in occurences:
    #     occurence_nb = occurences[word]
    #     if occurence_nb > maximum:
    #         maximum = occurence_nb
    #         word_maximum = word

    return word_maximum


def get_most_frequent_word3(words: list[str]) -> str:
    occurences = {}  # key: word, value: nb of occurences
    for word in words:
        try:
            occurences[word] = occurences[word] + 1
        except KeyError:
            occurences[word] = 1

    print(occurences)

    maximum = 0
    word_maximum = None
    for word, occurence_nb in occurences.items():
        if occurence_nb > maximum:
            maximum = occurence_nb
            word_maximum = word

    # for word in occurences:
    #     occurence_nb = occurences[word]
    #     if occurence_nb > maximum:
    #         maximum = occurence_nb
    #         word_maximum = word

    return word_maximum


def get_most_frequent_word3(words: list[str]) -> str:
    occurences = {}  # key: word, value: nb of occurences
    for word in words:

        occurences[word] = occurences.get(word, 0) + 1

    print(occurences)

    maximum = 0
    word_maximum = None
    for word, occurence_nb in occurences.items():
        if occurence_nb > maximum:
            maximum = occurence_nb
            word_maximum = word

    # for word in occurences:
    #     occurence_nb = occurences[word]
    #     if occurence_nb > maximum:
    #         maximum = occurence_nb
    #         word_maximum = word

    return word_maximum


def get_most_frequent_word3(words: list[str]) -> str:
    occurences = Counter(words)
    return occurences.most_common()[0]


print(get_most_frequent_word3(words))


# dict[str, int]

print(locals())
