pr = int(input('\033[35mPrimeiro termo: '))
razão = int(input('Razão: '))
s = 0
print('\033[1;34mGERADOR DE PA 2.0')
print('\033[1;38m-=' * 15)
print(f'\033[36m{pr} -> ', end='')
while s < 9:
    print('{} -> '.format(pr+razão), end='')
    s += 1
    pr += razão
print('FIM')
