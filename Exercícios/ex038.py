n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
if n1 > n2:
    print('\033[33mO número {} é maior que {}.'.format(n1, n2))
elif n1 < n2:
    print('\033[35mO número {} é maior que {}.'.format(n2, n1))
else:
    print('\033[36mOs dois valores são iguais.')
