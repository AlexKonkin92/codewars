s = "madam"


def pallindr(str):
    em_str = ""
    num = 0
    for b in reversed(list(str)):
        if str[num] != b:
            return "not pall"
        else:
            em_str += str[num]
            num += 1
    return em_str


print(pallindr(s))


s = "madamqq"
print(s == s[::-1])
