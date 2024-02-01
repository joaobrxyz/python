n1 = int(input('\033[35mDigite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais número: '))
n4 = int(input('Digite o último número: '))
n = n1, n2, n3, n4
print(f'\033[1;38mVocê digitou os valores: {n}')
print(f'\033[1;34mO valor 9 apareceu {n.count(9)} vezes.')
if n.count(3) > 0:
    print(f'\033[1;32mO valor 3 apareceu na {n.index(3) + 1}º posição.')
else:
    print('\033[1;31mO valor 3 não foi digitado em nenhuma posição.')
print('\033[1;36mOs valores pares digitados foram: ', end='')
for c in range(0, 4):
    if n[c] % 2 == 0:
        print(f'{n[c]}', end=' ')
