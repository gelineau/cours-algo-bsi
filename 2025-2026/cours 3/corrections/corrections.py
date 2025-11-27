from __future__ import annotations


######################################
# 1- nième caractère d’une chaîne
# Ecrire une fonction qui prend une chaîne de caractères en entrée,
# et qui renvoie "OK" si le deuxième caractère est égal au dernier
# caractère, et sinon "KO"
######################################


def check_chars(s: str) -> str:
    if s[1] == s[-1]:
        return "OK"
    else:
        return "KO"


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
# 3- Ecrire une fonction qui prend en paramètres un mot et une liste de mots.
# La fonction doit retourner la position du mot dans la liste de mots.
######################################


def find_word_position(word_to_find: str, words: list[str]) -> int | None:
    for i in range(len(words)):
        if words[i] == word_to_find:
            return i
    return None


def find_word_position(word_to_find: str, words: list[str]) -> int | None:
    for i, word in enumerate(words):
        if word == word_to_find:
            return i
    return None


######################################
# 4- Générer la liste ['ad', 'ae', 'bd', 'be', 'cd', 'ce']
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
# 5- Ecrire une fonction qui lit un fichier, et qui calcule pour chaque ligne :
# le nombre de caractères, le nombre de mots, et le hash md5 de la ligne
# Enregistrez ces résultats dans un nouveau fichier “résumé”
######################################

import hashlib


def summarize_file(file_path: str) -> list[list[str | int]]:
    summary = []
    with open(file_path, "r") as f:
        for line in f:
            num_letters = len(line)
            num_words = len(line.split())
            md5_hash = hashlib.md5(line.encode("utf-8")).hexdigest()
            summary.append([num_letters, num_words, md5_hash])
    return summary


def save_summary(summary: list[list[str | int]], output_file: str) -> None:
    """
    Saves the summary (list of lists) into a text file.
    Each line contains: Line X: Letters=..., Words=..., MD5=...
    """
    with open(output_file, "w") as f:
        for i, line_summary in enumerate(summary):
            letters, words, md5 = line_summary
            f.write(f"Line {i+1}: Letters={letters}, Words={words}, MD5={md5}\n")


print(f"{summarize_file("correction_lists.py")}")
save_summary(summarize_file("correction_lists.py"), "résumé.txt")


def have_common_line(file1: str, file2: str) -> bool:
    """
    Checks if there is at least one identical line (based on md5 hash) in both files.
    """
    summary1 = summarize_file(file1)
    summary2 = summarize_file(file2)
    for _, _, md5_1 in summary1:
        for _, _, md5_2 in summary2:
            if md5_1 == md5_2:
                return True
    return False


def have_common_line(file1: str, file2: str) -> bool:
    """
    Checks if there is at least one identical line (based on md5 hash) in both files.
    """
    summary1 = summarize_file(file1)

    hashes1 = set()
    for _, _, md5_1 in summary1:
        hashes1.add(md5_1)

    summary2 = summarize_file(file2)
    for _, _, md5_2 in summary2:
        if md5_2 in hashes1:
            return True
    return False


print(f"{have_common_line("correction_lists.py", "résumé.txt")=}")
print(f"{have_common_line("correction_lists.py", "../fait_en_cours.py")=}")

######################################
# 6. Fichier de logs
######################################


def get_url_paths(file_path: str) -> list[str]:
    urls = []
    with open(file_path) as file_obj:
        for line in file_obj:
            if line.startswith("POST"):
                # Example: 'POST /sysbus/NMC:getWANStatus HTTP/1.1'
                verb, path, version = line.split()
                if path not in urls:
                    urls.append(path)
    return urls


def get_url_paths(file_path: str) -> set[str]:
    urls = set()
    with open(file_path) as file_obj:
        for line in file_obj:
            if line.startswith("POST"):
                # Example: 'POST /sysbus/NMC:getWANStatus HTTP/1.1'
                verb, path, version = line.split()
                urls.add(path)
    return urls


def count_url_paths(file_path: str) -> dict[str, int]:
    url_counts = {}
    with open(file_path) as file_obj:
        for line in file_obj:
            if line.startswith("POST"):
                # Example: 'POST /sysbus/NMC:getWANStatus HTTP/1.1'
                verb, path, version = line.split()
                # url_counts[path] = url_counts.get(path, 0) + 1
                if path in url_counts:
                    url_counts[path] += 1
                else:
                    url_counts[path] = 1
    return url_counts


from collections import Counter


def count_url_paths(file_path: str) -> Counter:
    url_counter = Counter()
    with open(file_path, encoding="utf-8") as file_obj:
        for line in file_obj:
            if line.startswith("POST"):
                # Example: 'POST /sysbus/NMC:getWANStatus HTTP/1.1'
                verb, path, version = line.split()
                url_counter[path] += 1
    return url_counter


######################################
# 7. Demander des mots à l’utilisateur, pour chaque mot afficher sa taille.
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
# 8- Générer des mots de passe robustes
#   1. Ecrire une fonction qui génère un mot de passe d’une taille donnée,
#   composé de minuscules, majuscules, chiffres et caractères spéciaux
#   (au moins un caractère de chaque type). (utiliser le module Python random)
#   2. Demandez le nombre de mots de passe voulus, les générer et les écrire
#   dans un fichier texte
######################################

import random
import string


def generate_password(length: int) -> str:
    """
    Generates a strong password of the given length,
    containing at least one lowercase letter, one uppercase letter,
    one digit, and one special character.
    """

    # Ensure at least one character from each required type
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(string.punctuation)

    # Fill the rest of the password length with random characters from all types
    all_chars = string.ascii_letters + string.digits + string.punctuation
    others = [random.choice(all_chars) for _ in range(length - 4)]

    # Combine all characters and shuffle
    password_list = [lower, upper, digit, special] + others
    random.shuffle(password_list)
    return "".join(password_list)


def generate_passwords_to_file(
    nb_passwords: int, length: int, output_file: str
) -> None:
    """
    Generates nb_passwords strong passwords of the given length
    and writes them to a text file, one password per line.
    """
    with open(output_file, "w") as f:
        for _ in range(nb_passwords):
            password = generate_password(length)
            f.write(password + "\n")


nb = int(input("How many passwords do you want to generate? "))
size = int(input("What length for each password? "))
generate_passwords_to_file(nb, size, "passwords.txt")

######################################
# 9. Tester la complexité d’un mot de passe
######################################


def evaluate_password_strength(password: str) -> str:
    """
    Evaluates the strength of a password and returns a qualitative label.
    - Lowercase: 1 point
    - Uppercase: 2 points
    - Digit: 3 points
    - Special character: 4 points
    - Length multiplier:
        <6: x1
        6-8: x1.5
        9-11: x2
        12+: x2.5
    """
    score = 0
    for char in password:
        if char.islower():
            score += 1
        elif char.isupper():
            score += 2
        elif char.isdigit():
            score += 3
        else:
            score += 4  # special character

    # Length multiplier
    length = len(password)
    if length < 6:
        multiplier = 1
    elif 6 <= length <= 8:
        multiplier = 1.5
    elif 9 <= length <= 11:
        multiplier = 2
    else:
        multiplier = 2.5

    total_score = score * multiplier

    # Qualitative label
    if total_score < 20:
        label = "very weak"
    elif total_score < 35:
        label = "weak"
    elif total_score < 50:
        label = "medium"
    elif total_score < 70:
        label = "complex"
    else:
        label = "very complex"

    return label


def is_password_in_dictionary(password: str, dictionary_file: str) -> bool:
    """
    Checks if the given password exists in the dictionary file.
    Each line in the file should contain one password.
    """
    with open(dictionary_file, encoding="utf-8") as f:
        for line in f:
            if password == line.strip():
                return True
    return False

LETTER_VALUES = {
    'A': 2, 'B': 8, 'C': 4, 'D': 4, 'E': 1, 'F': 7, 'G': 8, 'H': 9, 'I': 2,
    'J': 9, 'K': 10, 'L': 3, 'M': 5, 'N': 2, 'O': 3, 'P': 4, 'Q': 7, 'R': 2,
    'S': 2, 'T': 2, 'U': 2, 'V': 6, 'W': 10, 'X': 10, 'Y': 10, 'Z': 10
}

def letter_value(char: str) -> int:
    """
    Returns the value of a letter based on its rarity in French.
    Non-letters (digits, special chars) can be assigned a default value.
    """
    if char.isalpha():
        return LETTER_VALUES.get(char.upper(), 10)
    elif char.isdigit():
        return 5
    else:
        return 7  # for special characters


######################################
# 10. Le classement FIFA
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
# 11. Listes imbriquées
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
# 12. Même question si les listes de départ peuvent avoir une profondeur quelconque
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
