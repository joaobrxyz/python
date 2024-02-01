from random import randint


def números():
    numeros = list()
    soma = 0
    for n in range(1, 6):
        sort = randint(1, 10)
        numeros.append(sort)
        del sort
    print(f'\033[1;34mSorteando 5 valores da lista: ', end='')
    print(*numeros, sep=', ', end=' ')
    print(f'PRONTO!')
    for n in numeros:
        if n % 2 == 0:
            soma += n
    print(f'\033[1;36mSomando os valores pares de {numeros}, temos {soma}.')


números()
