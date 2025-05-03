str_n = "Success"


def duplicate_encode(word):
    empty_str = ""
    str_list = list(word.lower())
    for i in str_list:
        if str_list.count(i) > 1:
            empty_str += ")"
        else:
            empty_str += "("
    return empty_str


print(duplicate_encode(str_n))
