from collections import deque


def convert_to_10(q):
    for i in range(len(q)):
        if q[i] == 'A':
            q[i] = 10
        elif q[i] == 'B':
            q[i] = 11
        elif q[i] == 'C':
            q[i] = 12
        elif q[i] == 'D':
            q[i] = 13
        elif q[i] == 'E':
            q[i] = 14
        elif q[i] == 'F':
            q[i] = 15
    return q


def convert_to_16(s):
    for i in range(len(s)):
        if s[i] == 10:
            s[i] = 'A'
        elif s[i] == 11:
            s[i] = 'B'
        elif s[i] == 12:
            s[i] = 'C'
        elif s[i] == 13:
            s[i] = 'D'
        elif s[i] == 14:
            s[i] = 'E'
        elif s[i] == 15:
            s[i] = 'F'
    return s


def sum_16_nums(a, b):
    a.reverse()
    b.reverse()
    result = deque()
    a_10 = convert_to_10(a)
    b_10 = convert_to_10(b)
    if len(a_10) >= len(b_10):
        for i in range(len(a_10) - len(b_10)):
            b_10.append(0)
    else:
        for i in range(len(b_10) - len(a_10)):
            a_10.append(0)
    c, d, e = 0, 0, 0
    for i in range(len(a_10)):
        d = int(a_10[i]) + int(b_10[i]) + c
        if d >= 16:
            c = 1
            e = d % 16
        else:
            e = d
            c = 0
        result.append(e)
    if c > 0:
        result.append(c)
    result.reverse()
    print(list(convert_to_16(result)))


a = deque(input('Введите шестнадцатиричное число: '))
b = deque(input('Введите шестнадцатиричное число: '))
sum_16_nums(a, b)

