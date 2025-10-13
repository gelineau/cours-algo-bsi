def count_vowels(sentence: str) -> int:
    vowels = "aeiouy"
    vowels += vowels.upper()

    counter = 0
    for character in sentence:
        if character in vowels:
            # counter = counter + 1
            counter += 1
    return counter


sentence = "Aspirine A"
number_of_wowels = count_vowels(sentence)
print(number_of_wowels)


def check_if_palindrome(sentence: str) -> bool:
    # for index in range(len(sentence) // 2):
    #     end_index = -index - 1
    #     if sentence[index] != sentence[end_index]:
    #         return False
    # return True
    return sentence == sentence[::-1]


print(f"{check_if_palindrome("abcba")=} {check_if_palindrome("abcbaa")=}")
