from random import randint
na = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
print(f'\033[1;34mOs valores sorteados foram: ', end='')
for c in range(0, 5):
    print(f'{na[c]}', end=' ')
print(f'\n\033[1;32mO maior número é {max(na)}')
print(f'\033[1;31mO menor número é {min(na)}')
