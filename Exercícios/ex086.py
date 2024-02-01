lista = [[], [], []]
for c in range(0, 3):
    di = int(input(f'Digite um valor para [0, {c}]: '))
    lista[0].append(di)
for c in range(0, 3):
    di = int(input(f'Digite um valor para [1, {c}]: '))
    lista[1].append(di)
for c in range(0, 3):
    di = int(input(f'Digite um valor para [2, {c}]: '))
    lista[2].append(di)
while True:
    for c in range(0, 3):
        print(f'[  {lista[0][c]}  ]', end='')
    print('')
    for c in range(0, 3):
        print(f'[  {lista[1][c]}  ]', end='')
    print('')
    for c in range(0, 3):
        print(f'[  {lista[2][c]}  ]', end='')
    break
