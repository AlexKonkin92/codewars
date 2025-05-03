a = "indivisibility"
b = "aA11"


def assert_equals(a):
    return len(set(i for i in list(a.lower()) if list(a.lower()).count(i) > 1))


print(assert_equals(b))
