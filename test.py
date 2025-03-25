def some_nums(*args):
    print(type(args))
    return args[1]


print(some_nums(1, 2, 6, 7))
print(type(some_nums(1, 2)))

# Дана строка, состоящая из букв 'X', 'Y' и 'O'. Необходимо найти кратчайшее расстояние между буквами 'X' и 'Y', либо вывести 0, если 'X' либо 'Y' отсутствуют.
# Примеры:
# "YY" -> 0
# "XX" -> 0
# "XY" -> 1
# "YOX" -> 2
# "OOOXOOYOXO" -> 2
# "OOOXXOY"-> 2


def likes(names):
    i = len(names)
    if i == 1:
        return f"{names[i-i]} likes this"
    if i == 2:
        return f"{names[i-i]} and {names[i-1]} like this"
    if i == 3:
        return f"{names[i-i]}, {names[i-2]} and {names[i-1]} like this"
    if len(names) >= 4:
        return f"{names[i-i]}, {names[i-(i-1)]} and {str((i-2))} others like this"
    else:
        return "no one likes this"


names = ["Max", "John", "Mark"]
print(likes(names))


def spin_words(sentence):
    i = 0
    lst = []
    str_v = ""
    while i < len(sentence):
        if sentence[i] != " ":
            lst.append(sentence[i])
        else:
            if len(lst) >= 5:
                for rev in list(reversed(lst)):
                    str_v += rev
                str_v += " "
                lst = []
            else:
                for nor in lst:
                    str_v += nor
                str_v += " "
                lst = []
        i += 1
    if len(lst) >= 5:
        for rev in list(reversed(lst)):
            str_v += rev
    else:
        for nor in lst:
            str_v += nor
    return str_v

    # lst = []
    # str_v = ""
    # for i in sentence:
    #     if i != " ":
    #         lst.append(i)
    #         # print (lst)
    # else:
    #     if len(lst) >= 5:
    #         for rev in list(reversed(lst)):
    #             str_v += rev
    #         str_v += " "
    #         lst = []
    #         # print(str_v)
    #     else:
    #         for nor in lst:
    #             str_v += nor
    #         str_v += " "
    #         lst = []
    #             # print(str_v)
    #         for lst_last in lst:

    # return str_v


def spin_words_new(sentence):
    sent_new = sentence.split()
    lst = []
    for i in sent_new:
        if len(i) >= 5:
            lst.append(i[::-1])
        else:
            lst.append(i)
    return " ".join(lst)


sentence = "This is"
print(spin_words_new(sentence))
