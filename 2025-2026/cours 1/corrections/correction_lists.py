from __future__ import annotations

######################################
# Manipulation de listes et de chaînes
######################################

# 1. Recevoir une phrase : Afficher chaque mot, avec son rang et sa taille.


def display_words(sentence: str) -> None:
    """Display each word with its position and length."""
    for i, word in enumerate(sentence.split(), start=1):
        print(f"{i}: {word} ({len(word)} characters)")


display_words("Hello to all students")

######################################
# 2. Construire une nouvelle liste constituée du double de chaque élément de la liste de départ.
# Avec une boucle, puis avec une list comprehension
######################################


def double_list(numbers: list[int]) -> list[int]:
    """Return a new list with each element doubled."""
    new_list = []
    for number in numbers:
        new_list.append(number * 2)
    return new_list


print(double_list([1, 2, 3]))


def double_list(numbers: list[int]) -> list[int]:
    """Return a new list with each element doubled."""
    return [number * 2 for number in numbers]


print(double_list([1, 2, 3]))

######################################
# 3. Rechercher si une valeur est présente dans une liste d’entiers.
# 3.2. Faire aussi une version avec une boucle sans utiliser les fonctions de recherche.
######################################


def search_number(numbers: list[int], number_to_find: int) -> bool:
    """
    Find if a value is present in a list of integers
    Complexity: O(n)
    """
    for number in numbers:
        if number == number_to_find:
            return True

    return False


def search_number(numbers: list[int], number_to_find: int) -> bool:
    return number_to_find in numbers


######################################
# 3. Rechercher si une valeur est présente dans une liste d’entiers.
# 3.2. Faire aussi une version avec une boucle sans utiliser les fonctions de recherche.
######################################


def search_position(numbers: list[int], number_to_find: int) -> int | None:
    """
    Find at which position a value is present in a list of integers
    Complexity: O(n)
    """
    for index in range(len(numbers)):
        number = numbers[index]
        if number == number_to_find:
            return index
    return None


def search_position(numbers: list[int], number_to_find: int) -> int | None:
    """
    Find at which position a value is present in a list of integers
    Complexity: O(n)
    """
    if number_to_find in numbers:
        return numbers.index(number_to_find)
    return None


######################################
# 5. Calculer la moyenne d’une liste d’entiers (en utilisant sum et sans l’utiliser).
######################################


def calculate_mean(numbers: list[int]) -> float:
    """
    Calculate the mean of a list of integers
    Complexity: O(n)
    """
    sum = 0
    for number in numbers:
        sum += number
    return sum / len(numbers)


def calculate_mean(numbers: list[int]) -> float:
    """
    Calculate the mean of a list of integers
    Complexity: O(n)
    """
    return sum(numbers) / len(numbers)


######################################
# 6. Insérer un élément au milieu d’une liste d’entiers
# (à une position donnée) (en utilisant insert et sans l’utiliser).
######################################


def insert_element(numbers: list[int], value: int, position: int):
    """Return a new list with value inserted at the given position."""
    numbers.insert(position, value)


def insert_element_no_insert(
    numbers: list[int], value: int, position: int
) -> list[int]:
    """Return a new list with value inserted at the given position (without insert)."""
    return numbers[:position] + [value] + numbers[position:]


######################################
# 7. Dans une liste d’entiers, remplacer chaque zéro par la somme
# de tous les entiers qui se trouvent avant lui.
######################################
def calculate_sum(numbers: list[int]) -> int:
    """
    Calculate the sum of a list of integers
    Complexity: O(n)
    """
    sum = 0
    for number in numbers:
        sum += number
    return sum


def replace_zero_by_rolling_sum(my_numbers: list[int]):
    """
    Replace each zero by the sum of all integers before it
    Version 1:
    Complexity: O(n^2)
    """
    for index in range(len(my_numbers)):
        if my_numbers[index] == 0:
            rolling_sum = calculate_sum(my_numbers[:index])
            my_numbers[index] = rolling_sum


def replace_zero_by_rolling_sum2(my_numbers: list[int]):
    """
    Replace each zero by the sum of all integers before it
    Version 2:
    Complexity: O(n)
    """
    rolling_sum = 0
    for index in range(len(my_numbers)):
        if my_numbers[index] == 0:
            my_numbers[index] = rolling_sum
        rolling_sum += my_numbers[index]


my_numbers = [1, 2, 0, 8, 4, 0]

print(
    f"""
{search_number(my_numbers, 2)=}
{search_number(my_numbers, 12)=}
{search_position(my_numbers, 8)=}
{calculate_mean(my_numbers)=}
"""
)

replace_zero_by_rolling_sum(my_numbers)
print(my_numbers)

my_numbers = [1, 2, 0, 8, 4, 0]
replace_zero_by_rolling_sum2(my_numbers)
print(my_numbers)

######################################
# 8- Générer la liste ['ad', 'ae', 'bd', 'be', 'cd', 'ce']
# à partir des chaînes "abc" et "de" (avec 2 boucles ou avec une list comprehension).
######################################


def combinations(string1: str, string2: str) -> list[str]:
    """Return all combinations of one character from string1 and one from string2."""
    result = []
    for character1 in string1:
        for character2 in string2:
            result.append(character1 + character2)
    return result


print(combinations("abc", "de"))


def combinations(string1: str, string2: str) -> list[str]:
    """Return all combinations of one character from string1 and one from string2."""
    return [character1 + character2 for character1 in string1 for character2 in string2]


print(combinations("abc", "de"))


######################################
# 9. Demander des mots à l’utilisateur, pour chaque mot afficher sa taille.
# S’interrompre quand il saisit “fin” en utilisant l’instruction break.
######################################


def words_and_lengths() -> None:
    """Ask the user for words and display their length, stop when 'fin' is entered."""
    while True:
        word = input("Mot (entrez 'fin' pour arrêter) : ")
        if word == "fin":
            break
        print(f"{word} ({len(word)} characters)")


######################################
# 10. Utilisez l’instruction continue pour afficher tous les mots d’une phrase,
# sauf le 5ième, le 10ième, etc.
######################################


def remove_every_5th_word(sentence: str) -> list[str]:
    """return all words except the 5th, 10th, etc."""
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
# 11. Le classement FIFA
######################################

teams = ["Brésil", "Argentine", "Allemagne", "Chili", "Belgique"]
scores = [1635, 1529, 1433, 1386, 1371]

for i, (country, points) in enumerate(zip(teams, scores)):
    print(i + 1, country, ":", points, "points")

for i, (country, points) in enumerate(zip(teams, scores), start=1):
    print(i, country, ":", points, "points")

for i, country, points in zip(range(1, len(teams) + 1), teams, scores):
    print(i, country, ":", points, "points")


######################################
# 12. Listes imbriquées
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
print(merge_and_tuple(a, b))


######################################
# 13. Même question si les listes de départ peuvent avoir une profondeur quelconque
######################################


def deep_flatten(nested: list) -> list[int]:
    """
    Recursively flatten a nested list of integers.
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
