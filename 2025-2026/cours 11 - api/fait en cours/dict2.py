# 1 - créer un dictionnaire simple
# Ecrire une fonction qui retourne un dictionnaire contenant un seul élément
# dont la clé est 27 et la valeur est [1,2,3]


def create_simple_dict() -> dict[int, list[int]]:
    return {27: [1, 2, 3]}


# itérer sur un dict
# écrire une fonction qui reçoit en paramètre un dict[str, float]
# et qui calcule le produit de toutes les valeurs
# 2.3 4.5 6.8  => 2.3*4.5*6.8


def calculate_product_of_values(my_dict: dict[str, float]) -> float:
    result = 1
    for key, value in my_dict.items():
        result *= value
    return result


# à partir de ["cochon", "chien", "vache"] créer un dictionnaire dont la clé
# est le mot et la valeur est la position du c dans le mot
# ("cochon".index("c") => 0)


def create_position_dictionary(words: list[str]) -> dict[str, int]:
    position_dictionary = {}
    for word in words:
        position_dictionary[word] = word.index("c")
    return position_dictionary


def create_position_dictionary(words: list[str]) -> dict[str, int]:
    return {word: word.index("c") for word in words}
