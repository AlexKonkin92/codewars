def count_AGTC(n):
    empty_list = []
    new_list = list(n)
    empty_list.append(new_list.count("A"))
    empty_list.append(new_list.count("G"))
    empty_list.append(new_list.count("T"))
    empty_list.append(new_list.count("C"))
    return tuple(empty_list)


print(count_AGTC("AGTTTTT"))
