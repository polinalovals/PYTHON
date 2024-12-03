def fibonacci_r(n, a=1, b=1):
    if n > 0:
        print(a, end=' ')
        fibonacci_r(n - 1, b, a + b)


def fibonacci_i(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        print(a, end=' ')


fibonacci_i(10)
print()
fibonacci_r(10)
