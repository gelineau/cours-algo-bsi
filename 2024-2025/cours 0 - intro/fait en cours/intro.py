# # age = 3
# # pay = 2345.34
# # age = 234.2
# #
# # # of course!
# # print(12 < 5)
# # is_smaller = 12 < 5
# # print(f"{is_smaller=}")
#
# my_string = "coucou"
# my_string = 'couc"ou'
# my_string = """
# usage:
#    --help: prints help
#    --cut: keep first column
# """
#
# my_string = "RENNES"
# print(my_string[1:4] + my_string[4:5])
# print(my_string[1:5])
# # print(len(my_string[1:5]) == 5 - 1)
# #
# # print(f"{len(my_string[1:25])=}")
# # print(f"{'E' in my_string=}")
# # print(f"{'Z' in my_string=}")
# # # print(f"{'ENN' in my_string=}")
# # my_string = "Bonjour, il fait, très chaud, aujourd'hui"
# # best_number = 35
# # print(f"{my_string} est dans le département {best_number:33}")
# # print(my_string, " est dans le département ", best_number)
# #
# # print(len(my_string.split()))
#
# # my_list = [1, 2, 4, "RENNES", True]
#
# # print(my_list[4])
# # print(my_list[2:3])
#
# my_list = []
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# my_list.append("fin")
#
# print(my_list[3])
# my_list[3] = 4
# print(my_list)
#
# my_list = my_list[:3] + [3, 5, 6]
# print(my_list)


# age = 190
#
# if age > 18:
#     print("tu peux boire")
#     print("tu peux voter")
#     if age > 100:
#         print("pas trop d'alcool")
#
# print("au revoir")
#
#
# animals = ["chien", "chat", "lapin"]
#
# for animal in animals:
#     print(animal, len(animal))
#
#
# for number in range(11):
#     print(number)


TAXES_RATE = 21


def calculate_price_with_taxes(price_without_taxes: float) -> float:
    if price_without_taxes == 0:
        return -1
    price_with_taxes = price_without_taxes * (1 + TAXES_RATE / 100)
    return price_with_taxes


price1 = 14
new_price1 = calculate_price_with_taxes(price1)
print(new_price1)

price2 = 15
new_price2 = calculate_price_with_taxes(price2)
print(new_price2)
