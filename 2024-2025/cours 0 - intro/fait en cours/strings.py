def detect_palyndrom(word: str) -> bool:
    # length = len(word)
    # for index in range(length):
    #     end_index = length - 1 - index
    #     if word[index] != word[end_index]:
    #         return False
    # return True
    reversed_word = word[::-1]
    return word == reversed_word


print(detect_palyndrom("ABCDCBA"))
print(detect_palyndrom("ABCDZBA"))
