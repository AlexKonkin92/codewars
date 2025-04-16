seq = [0, 1, 0, 1, 0]


def find_it(seq):
    set_array = set(seq)
    for i in set_array:
        cnt = seq.count(i)
        if cnt % 2 == 0:
            continue
        else:
            return i


print(find_it(seq))


seq = [0, 1, 0, 1, 0]
dict = {}


def find_it2(seq):
    for i in seq:
        if i in dict:
            num = dict[i]
            num += 1
            dict[i] = num
        else:
            dict[i] = 1
    for k, v in dict.items():
        if v % 2 != 0:
            return k


print(find_it2(seq))


seq = [0, 1, 0, 1, 0]


def find_it2(seq):
    for i in seq:
        if seq.count(i) % 2 != 0:
            return i


for i in seq:
    print(i)
print(find_it2(seq))
