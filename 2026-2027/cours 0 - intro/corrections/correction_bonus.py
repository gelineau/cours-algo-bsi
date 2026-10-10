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
