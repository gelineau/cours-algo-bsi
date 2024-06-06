# create an empty dictionary
frequency = {}

# add elements

frequency["le"] = 10
frequency["du"] = 15
frequency["pour"] = 5

# print dictionary

print(frequency)

# search a value
print(frequency["du"])

# update a value (no duplicated keys)
frequency["du"] = 16
print(frequency["du"])

# iterate on the dictionary
for word, number in frequency.items():
    print(f"{word=} {number=}")
