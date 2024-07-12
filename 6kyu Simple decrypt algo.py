import re


def decrypt(test_key):
    clear_str = re.sub('[^a-z]', '', test_key)  # оставляем только буквы
    dict = {}
    new_str = []
    for i in clear_str:
        dict[i] = clear_str.count(i)
    alphabet = [chr(i) for i in range(97, 123)]
    for i in alphabet:
        if i in dict:
            new_str.append(str(dict[i]))
        else:
            new_str.append('0')
    return (''.join(new_str))


def decrypt2(test_key):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    s = ''
    for n in alpha:
        s += str(test_key.count(n))
    return s


if __name__ == "__main__":
    city = 'z$aaa#ccc%eee1234567890'
    print(decrypt(city))
