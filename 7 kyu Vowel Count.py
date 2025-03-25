def get_count2(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    return sum(1 for i in list(sentence) if i in vowels)


print(get_count2(string_v))
