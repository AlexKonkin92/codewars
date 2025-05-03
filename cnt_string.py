s = "ss dddd dsasda q"
# new_s = s.upper().split(" ")
# n = 0
# str_print = ''


def cnt_str(s):
    new_s = s.upper().split(" ")
    n = 0
    str_print = ""
    for str in new_s:
        if str.count(str[0]) == len(str) and len(str) > n:
            str_print = str
            n = len(str)
    return str_print


print(cnt_str(s))
