lista = [[], [], []]
par = tc = mai = 0
for c in range(0, 3):
    di = int(input(f'\033[1;35mDigite um valor para [0, {c}]: '))
    lista[0].append(di)
for c in range(0, 3):
    di = int(input(f'Digite um valor para [1, {c}]: '))
    lista[1].append(di)
for c in range(0, 3):
    di = int(input(f'Digite um valor para [2, {c}]: '))
    lista[2].append(di)
print('\033[1;36m=-' * 35)
for c in range(0, 3):
    print(f'\033[1;33m[  {lista[0][c]}  ]', end='')
print('\033[1;33m')
for c in range(0, 3):
    print(f'[  {lista[1][c]}  ]', end='')
print('')
for c in range(0, 3):
    print(f'[  {lista[2][c]}  ]', end='')
print('')
print('\033[1;36m=-' * 35)
for c in lista:
    for p in c:
        if p % 2 == 0:
            par += p
for tl in lista[2]:
    tc += tl
for c in range(0, 3):
    mai += lista[c][2]
print(f'\033[1;34mA soma dos valores pares é {par}.')
print(f'A soma dos valores da terceira coluna é {mai}.')
print(f'O maior valor da segunda linha é {max(lista[1])}.')
