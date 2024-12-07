from operator import length_hint


def fakt(x):
    if x == 1:
        return 1
    return fakt(x - 1) * x


print(fakt(4))


def fib_r_2(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fib_r_2(n - 1) + fib_r_2(n - 2)


print(fib_r_2(10))


def fib_r_3(n, a=0, b=1):
    if n == 1:
        return b
    if n == 2:
        return b + a
    return fib_r_3(n - 1, b, a + b)


print(fib_r_3(10))

# задача на палиндром #шалаш

my_sentence = 'i love this world'
my_list = list(my_sentence)  # превраащем нашу строку в список
print(my_list)


def searching_for_palindrom(sentence):
    my_list_sentence = list(sentence)
    return my_list_sentence == my_list_sentence[::-1]


print(searching_for_palindrom('пара'))


def palindrom(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return palindrom(s[1:-1])


# решение задач на палином и на ряд фиббоначи используя рекурсивные методы
def fib_new(n, a=0, b=1):
    if n == 0:
        return a
    if n == 1:
        return b
    return fib_new(n - 1, b, a + b)  # как вернуть весь лист


print(fib_new(10))


# fibonacci only answer
def fibonacci_answer(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fibonacci_answer(n - 1) + fibonacci_answer(n - 2)


print(fib_new(10))


def polinom_untersuchung(sentance):
    my_list_1 = list(sentance)
    if len(my_list_1) <= 1:
        return True
    if my_list_1[0] != my_list_1[-1]:
        return False
    return polinom_untersuchung(my_list_1[1:-1])


print(polinom_untersuchung('шалаш'))

sentance = 'i love programmierung'
print(sentance[10:4:-1])


def factorial_untersuchung(n):
    if n == 1:
        return 1
    return factorial_untersuchung(n - 1) * n


print(factorial_untersuchung(4))

# есть строка, надо чтоб мы дошли до среедины и разделяли на ( а потом на )
sentance = 'abcdefhkj'


def unteruchung_satz(n):
    middle_satz = len(n) // 2
    if n[:middle_satz]:
        return unteruchung_satz(' '.join('f {element} (' for element in n))
    if n[middle_satz:]:
        return unteruchung_satz(' '.join('f {element} )' for element in n))
    if len(n) == middle_satz:
        return unteruchung_satz


print(unteruchung_satz('icheihtgv'))

print(unteruchung_satz('abcdefhkj'))
list = [True, 'nothing', 4, 7, 32, False]
print(' '.join(str(element) for element in list))
print(' '.join(f'{element} 9' for element in list))
