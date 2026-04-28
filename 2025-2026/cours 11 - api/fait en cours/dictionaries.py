import json
from pprint import pprint

inhabitants = {
    "paris": 1000,
    "rennes": 2,
    "nantes": 3,
    "tokyo": 344,
}


message = {
    "date": "2026",
    "packets": [
        {"id": 1, "data": [1, 5, 6]},
        {"id": 2, "data": [1, 8, 6]},
    ],
    "is_allowed": None,
}

pprint(message["packets"])
pprint(message["packets"][1])
pprint(message["packets"][1]["data"])
pprint(message["packets"][1]["data"][1])


def create_length_dictionary(words: list[str]) -> dict[str, int]:
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths


def create_length_dictionary(words: list[str]) -> dict[str, int]:
    return {word: len(word) for word in words}


animals = ["chien", "chat", "pinson"]
lengths = create_length_dictionary(animals)
print(lengths)


for key, value in lengths.items():
    print(f"{key=} {value=}")


# my_dict["chat"] ===> O(1)


print(json.dumps(message))


print(
    json.loads(
        """
{"date": "2026", "packets": [{"id": 1, "data": [1, 5, 6]}, {"id": 2, "data": [1, 8, 6]}], "is_allowed": null}
"""
    )
)
