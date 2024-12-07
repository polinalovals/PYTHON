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


def recursiv_number(a=input('geben sie eine zahel ein: '))
    for a == 0:
        return 0
    for a == 1:
        return 1
    return recursiv_number(int(elements) for elements in a)  # как то написать сумму


def recursiv_dis(a):
    if a < 10:
        return a
    else:
        return a % 10 + recursiv_dis(a // 10)


number = int(input("Geben Sie eine Zahl ein: "))
result = recursiv_dis(number)


def recursiv_dis(a=input('Geben Sie eine Zahl ein: ')):
    if len(a) == 0:
        return 0
    return int(a[0]) + recursiv_dis(a[1:])


result = recursiv_dis()
print(f"Die Summe der Ziffern ist: {result}")
