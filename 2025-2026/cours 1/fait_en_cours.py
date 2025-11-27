# https://github.com/gelineau/cours-algo-bsi
#


## Exo 1


def detail_words(sentence: str) -> None:
    words = sentence.split()
    # for index, word in enumerate(words):
    #     print(f"{index+1}: {word} ({len (word)})")
    for index in range(len(words)):
        word = words[index]
        print(f"{index+1}: {word} ({len (word)})")


sentence = "oh temps suspends ton vol"
detail_words(sentence)


def double_list(numbers: list[int]) -> list[int]:
    new_list = []

    for number in numbers:
        new_list.append(number * 2)

    return new_list


def double_list(numbers: list[int]) -> list[int]:
    new_list = [number * 2 for number in numbers]

    return new_list


my_list = [1, 4, 3]
new_list = double_list(my_list)
print(new_list)
