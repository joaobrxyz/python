lista = [[], []]
for c in range(1, 8):
    v = int(input(f'\033[1;35mDigite o {c}º valor: '))
    if v % 2 == 0:
        lista[0].append(v)
    else:
        lista[-1].append(v)
lista[0].sort()
lista[1].sort()
print('\033[1;38m=-' * 30)
print('\033[1;36mOs valores pares digitados foram: ', end='')
print(*lista[0], sep=', ')
print('\033[1;34mOs valores ímpares digitados foram: ', end='')
print(*lista[-1], sep=', ')
