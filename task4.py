# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
#qqqqrrrtt -> 4q3r2t
# 4q2w3eio2p -> qqqqwweeeiopp



def encode(st: str):
    res = ''
    i = 0
    while i < len(st):
        count = 1
        while i + 1 < len(st) and st[i] == st[i + 1]:
            count += 1
            i += 1
        res += str(count) + st[i]
        i += 1
    return res


def decode(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res += txt[i] * int(number)
            number = ''
    return res

st1 = 'qqqwwerttyyy'
print(encode(st1))
print(decode(encode(st1)))