from time import sleep


def contador():
    print('\033[1;33m-='* 30)
    print('\033[1;34mContagem de 1 até 10 de 1 em 1:')
    for c in range(1, 11, 1):
        print(f'\033[1;36m{c} ', end='')
        sleep(0.7)
    print('FIM!')
    print('\033[1;33m-='* 30)
    print('\033[1;34mContagem de 10 até 0 de 2 em 2:')
    for c in range(10, -1, -2):
        print(f'\033[1;36m{c} ', end='')
        sleep(0.7)
    print('FIM!')
    print('\033[1;33m-='* 30)
    print('\033[1;38mAgora é sua vez de personalizar a contagem!')
    início = int(input('\033[1;35mInício: '))
    fim = int(input('Fim: '))
    passo = int(input('Passo: '))
    print('\033[1;33m-='* 30)
    print(f'\033[1;38mContagem do {início} até {fim} de {passo} e {passo}:')
    if fim > 0:
        fim += 1
    elif fim <= 0:
        fim -= 1
    if passo < 0:
        passo *= 1
    elif passo == 0:
        passo = 1
    if início > fim and passo > 0:
        passo *= -1
    for c in range(início, fim, passo):
        print(f'\033[1;36m{c}, ', end='')
        sleep(0.7)
    print('FIM!')


contador()
