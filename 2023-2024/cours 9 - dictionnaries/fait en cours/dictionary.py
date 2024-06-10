# create an empty dictionary
occurence = {}

# add elements

# occurence["le"] = 55
# occurence["du"] = 5

occurence = {"le": 55, "du": 5}
occurence["troisieme"] = 45
# print dictionary

print(occurence)

# search a value

print(occurence["le"])

# update a value
occurence["le"] = 56

print(occurence)

if "non existant" in occurence:
    print(occurence["non existant"])
else:
    print("toto")


# iterate on the dictionary
print("*" * 80)
for word, nb_of_occurences in occurence.items():
    print(word, nb_of_occurences)
