# # # # price = 34 + 23
# # # # print(price, type(price))
# # # # price = 34 / 3
# # # # print(price, type(price))
# # # # #
# # # # # price = 11.333
# # # # # print(int(price))
# # # # #
# # # # # name = "hello"
# # # # # name = 'johnny a dit : "allumez le feu"'
# # # # # print(name)
# # # # # name = 'johnny a dit : "allumez le feu"'
# # # # # name = "Menu\n\t1- melon\n\t2- boeuf"
# # # # # print(name)
# # # name = "concombre"
# # # # print(len(name))
# # # # print(name[1])
# # # # print(name[8])
# # # # print(name[-1])
# # # # print(name[1:4])
# # # # print(name[1:-1])
# # # # print(name[0:3])
# # # # print(name[:3])
# # # # print(name[-3:9])
# # # # print(name[-3:])
# # #
# # # # does name contain a
# # #
# # # print("on" in name)
# # # print(name.startswith("con"))
# # #
# # # csv = "12,56,47"
# # # print(csv.split(","))
# # # sentence = "il fait beau aujourd'hui\twesh"
# # # print(sentence.split())
# #
# # name = "François"
# # age = 56
# # result = f"""bonjour {name},
# # est-ce vrai que tu as {age-1} ans"""
# # print(result)
# #
# #
# # print(type(23 < 34 and not (2 > 4)))
# #
# # # a = "24a"
# # # print(int(a))
# #
# #
# # print((str(23) + str(1)).split("3"))
# #
# # my_beautiful_list = [1, 2, "3", [2, 3]]
# # print(len(my_beautiful_list))
# # print(1 in my_beautiful_list)
# # print(my_beautiful_list[1])
# # print(my_beautiful_list[:3])
# #
# #
# # my_list = [1, 2, 3]
# # my_list[1] = "4"
# # print(my_list)
# #
# # my_list.append("fin")
# # print(my_list)
# #
# #
# #
# #
#
#
# age = 17
# #
# # if age < 18:
# #     print("tu es mineur")
# # else:
# #     print("majeur")
# #     entry = True
#
# ages = [1, 5, 34, 2, 18]
#
# for age in ages:
#     print(f"age = {age}")
#
# chars = "azertty"
# for char in chars:
#     if char != "t":
#         print(char)
#
# for index in range(len(chars)):
#     if index < len(chars) / 3:
#         print(f"index= {index} valeur={chars[index]}")
#
# print(f"len = {len(chars)}")
# print(f"range = {list(range(7))}")
#
#
#


def add_taxes(price: int, is_food: bool) -> int:
    if is_food:
        new_price = price * 1.05
    else:
        new_price = price * 1.2
    return int(new_price)


car_price = 10000
print(f"ttc voiture = {add_taxes(car_price, is_food=False)}")
house_price = 200_000
print(f"ttc maison = {add_taxes(house_price, is_food=False)}")
