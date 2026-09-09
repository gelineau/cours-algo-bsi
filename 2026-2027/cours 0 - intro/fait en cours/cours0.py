from __future__ import annotations

#
#
# name = "Gelineau"
#
# print(name[1])
# # print(name[100])
# print(name[7])
# print(name[-1])
#
#
# print(name[1:3])
# print(name[1:8])
# print(name[1:])
# print(name[1:-1])
# print(name[:5])
#
# print(name[7:200])
# print(name[:])
# print(len(name))
#
# print("i" in name)
# if "i" in name:
#     print("dedans")
# print("ine" in name)
#
# print("ab" + "cd")
# print("*" * 80)

sentence = "pikachu    est un \tpokemon électrique"
words = sentence.split()
# print(sentence.split("e"))
#
# print(words[1])
# print(len(words))
# print("pikachu" in words)
# print(words[1:-1])
#
# print(words[0][0])

# a = "67a"
#
# print(int(True))


def transform_to_dollar(price_euro: float | int) -> float:
    print("ca va ?")
    if price_euro < 0:
        print("t'es sûr ?")
        print("vraiment ?")
    return price_euro / 1.2


price_euro1 = 12.34
price_dollar1 = transform_to_dollar(price_euro1)
print(price_dollar1)

price_euro2 = 128
price_dollar2 = transform_to_dollar(price_euro2)
print(price_dollar2)

transform_to_dollar("azzeer")
