from __future__ import annotations

######################################
# Continue / break
######################################

######################################
# 9. Demander des mots à l'utilisateur, pour chaque mot afficher sa taille.
# S'interrompre quand il saisit "fin" en utilisant l'instruction break.
######################################


def words_and_lengths() -> None:
    """Ask the user for words and display their length, stop when 'fin' is entered."""
    while True:
        word = input("Mot (entrez 'fin' pour arrêter) : ")
        if word == "fin":
            break
        print(f"{word} ({len(word)} characters)")


######################################
# 10. Utilisez l'instruction continue pour afficher tous les mots d'une phrase,
# sauf le 5ième, le 10ième, etc.
######################################


def remove_every_5th_word(sentence: str) -> list[str]:
    """Return all words except the 5th, 10th, etc."""
    result = []
    words = sentence.split()
    for i, word in enumerate(words):
        if (i + 1) % 5 == 0:
            continue
        result.append(word)
    return result


print(
    remove_every_5th_word(
        "il était une fois, dans un petit village, un petit chaperon rouge"
    )
)


######################################
# zip / enumerate
######################################

######################################
# 11. Le classement FIFA
######################################

teams = ["Brésil", "Argentine", "Allemagne", "Chili", "Belgique"]
scores = [1635, 1529, 1433, 1386, 1371]

# Version 1: enumerate + zip, index commençant à 0 (on ajoute 1 à l'affichage)
for i, (country, points) in enumerate(zip(teams, scores)):
    print(i + 1, country, ":", points, "points")

# Version 2: enumerate + zip, avec start=1
for i, (country, points) in enumerate(zip(teams, scores), start=1):
    print(i, country, ":", points, "points")

# Version 3: zip de trois séquences, dont un range
for i, country, points in zip(range(1, len(teams) + 1), teams, scores):
    print(i, country, ":", points, "points")


######################################
# Listes imbriquées
######################################

######################################
# 12. Fusionner deux listes de listes, trier, puis grouper par paires
######################################


def merge_and_tuple(
    numbers1: list[list[int]], numbers2: list[list[int]]
) -> list[tuple[int, int] | tuple[int]]:
    """
    Merge two lists of lists, flatten, sort, and group into tuples of two elements.
    """
    flattened_list = []
    for sublist in numbers1 + numbers2:
        flattened_list.extend(sublist)

    flattened_list.sort()

    result = []
    for index in range(0, len(flattened_list), 2):
        if index == len(flattened_list) - 1:
            result.append((flattened_list[index],))
        else:
            result.append((flattened_list[index], flattened_list[index + 1]))
    return result


a = [[1, 4, 9], [2, 6], [11]]
b = [[3, 5], [7, 8, 10]]
print(merge_and_tuple(a, b))  # [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11,)]


######################################
# 13. Bonus : même question avec des listes de profondeur quelconque
######################################


def deep_flatten(nested: list) -> list[int]:
    """
    Recursively flatten a nested list of integers, whatever its depth.
    """
    result: list[int] = []
    for item in nested:
        if isinstance(item, list):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result


def merge_and_tuple_deep(
    numbers1: list, numbers2: list
) -> list[tuple[int, int] | tuple[int]]:
    """
    Merge two arbitrarily nested lists of integers, flatten, sort,
    and group into tuples of two elements (or one if odd).
    """
    flattened_list = deep_flatten(numbers1 + numbers2)
    flattened_list.sort()

    result = []
    for index in range(0, len(flattened_list), 2):
        if index == len(flattened_list) - 1:
            result.append((flattened_list[index],))
        else:
            result.append((flattened_list[index], flattened_list[index + 1]))
    return result


a = [[1, [2, [3, 5, [8]]]], [10, 11]]
b = [[4], [6, 7], 12]
print(merge_and_tuple_deep(a, b))

