# frequency = { "le": 10, "du": 15, "pour": 5}

frequency = {}

# add

frequency["le"] = 10
frequency["du"] = 15
frequency["pour"] = 5

print(frequency)

# fetch value
print(frequency["du"])

print(frequency.get("du"))
print(frequency.get("do", 42))


frequency["du"] = 16

print(frequency)

for word, number in frequency.items():
    print(f"le mot {word} apparait {number} fois")
