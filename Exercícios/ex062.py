pr = int(input('\033[35mPrimeiro termo: '))
razão = int(input('Razão: '))
s = 0
tot = 0
mais = 9
print('\033[1;34mGERADOR DE PA 2.0')
print('\033[1;38m-=' * 15)
print(f'\033[36m{pr} -> ', end='')
while mais != 0:
    tot += mais
    while s <= tot:
        print('{} -> '.format(pr+razão), end='')
        s += 1
        pr += razão
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar mais? '))
print('\033[1;32mProgressão finalizada com {} termos mostrados.'.format(s))
