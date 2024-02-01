from time import sleep


def maior(*lst):
    print('\033[1;33m-=' * 30)
    print(f'\033[1;34mAnalisando os valores passados...')
    for n in lst:
        sleep(0.4)
        print(f'\033[1;36m{n}', end=' ')
    print(f'\033[1;36mForam informados {len(lst)} valores ao todo.')
    if len(lst) > 0:
        print(f'\033[1;32mO maior valor informado foi {max(lst)}.')
    else:
        print(f'\033[1;32mO maior valor informado foi 0.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
