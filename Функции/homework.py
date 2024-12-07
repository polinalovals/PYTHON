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


print(norm_number('11001'))
