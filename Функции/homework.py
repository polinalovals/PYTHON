# Написать рекурсивную функцию, переводящую число в двоичное представление
# Предварительно написать функцию нерекурсивную с этим алгоритмом (без bin)

def norm_number(a):
    list_a = list(a)
    list_a.reverse()
    result = 0
    index_list_a = 0
    for i in list_a:
        result += int(i) * (2 ** index_list_a)
        index_list_a += 1
    return result

def binary(x):
    res = ''
    while x > 0:
        res = str(x % 2) + res
        x //= 2
    return res


def binary_rec(x):
    if x > 0:
        return binary_rec(x // 2) + str(x % 2)
    return ''


def to_dec(b, i=0):
    if len(b) > 0:
        return to_dec(b[:-1], i + 1) + int(b[-1]) * 2 ** i
    return 0


# print(binary_rec(24))
print(to_dec('10001110'))


def recursiv_number(a):
    if a == 0:
        return 0
    if a == 1:
        return 1
    return recursiv_number(int(elements) for elements in a)


def recursiv_dis(a):
    if a > 0:
        return a % 10 + recursiv_dis(a // 10)
    return 0


