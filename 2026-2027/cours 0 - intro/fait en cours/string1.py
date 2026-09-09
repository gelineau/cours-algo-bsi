def get_character(sentence: str, index: int) -> str | None:
    if index >= len(sentence) or index < -len(sentence):
        return None

    return sentence[index]


my_string = "Gelineau"
print(get_character(my_string, -9))
