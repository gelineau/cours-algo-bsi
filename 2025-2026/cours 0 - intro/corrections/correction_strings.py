def reformat_email(email: str) -> str:
    # Séparer la partie 1 (avant @) et la partie 2 (après @)
    part_1, part_2 = email.split("@")

    # Séparer le prénom et le nom
    first_name, last_name = part_1.split(".")

    # Séparer le domaine et le pays
    domain, country = part_2.split(".")

    # Reconstruire l'adresse email dans le nouveau format
    new_email = f"{last_name}.{first_name}@{domain}-pro.{country}"

    return new_email


# Exemple d'utilisation
new_email = reformat_email("jean.dupont@intradef.fr")
print(new_email)  # Affichera : dupont.jean@intradef-pro.fr


def count_vowels(sentence: str) -> int:
    # vowels = "aeiouyAEIOUY"
    vowels = "aeiouy"
    vowels += vowels.upper()
    number = 0
    for char in sentence:
        if char in vowels:
            number += 1
    return number
    # return sum(1 for char in sentence if char in vowels)


sentence = "Aspirine A"
number_vowels = count_vowels(sentence)
print(f"Il y a {number_vowels} voyelles dans cette phrase.")


def is_palindrome(sentence: str) -> bool:
    # Supprimer les espaces et convertir en minuscules
    # isalnum vérifie si le caractère est alphanumérique
    # clean = "".join(char.lower() for char in sentence if char.isalnum())
    # Vérifier si la chaîne nettoyée est égale à son inverse
    # return clean == clean[::-1]

    for index in range(len(sentence) // 2):
        if sentence[index] != sentence[len(sentence) - 1 - index]:
            return False
    return True


print(f"{is_palindrome('abcba')=} {is_palindrome('abba')=} {is_palindrome('cabbad')=}")


def reverse_chain(sentence: str) -> str:
    # return sentence[::-1]

    # return "".join(reversed(sentence))

    # reversed_string = ""
    # for char in sentence:
    #     reversed_string = char + reversed_string
    # return reversed_string

    reversed_string = ""
    for index in range(len(sentence)):
        reversed_string += sentence[len(sentence) - 1 - index]

    return reversed_string


# Test
print(reverse_chain("Python"))  # Sortie : nohtyP
