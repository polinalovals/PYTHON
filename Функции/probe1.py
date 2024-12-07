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
