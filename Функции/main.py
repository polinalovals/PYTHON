def print_seq(n):
    if n > 0:
        print(n, end=' ')
        print_seq(n - 1)


def sum_seq(n):
    if n > 0:
        return n + sum_seq(n - 1)
    return 0


print_seq(10)
print()
print(sum_seq(10))