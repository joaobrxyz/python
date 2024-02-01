from time import sleep
c = ('\033[m',        # 0 - sem cores
    '\033[0;30;41m',  # 1 - vermelho
    '\033[0;30;42m',  # 2 - verde
    '\033[0;30;43m',  # 3 - amarelo
    '\033[0;30;44m',  # 4 - azul
    '\033[0;30;45m',  # 5 - roxo
    '\033[7;40m'      # 6 - branco
     )


def superprint(str, cor=0):
    tot = len(str) + 4
    print(c[cor], end='')
    print(f'~' * tot)
    print(f'  {str}')
    print(f'~' * tot)
    print(c[0], end='')
    sleep(1)


def ajuda():
    while True:
        superprint('SISTEMA DE AJUDA PyHELP', 2)
        fb = str(input('Função ou Biblioteca → '))
        if fb.upper() in 'FIM':
            break
        superprint(f'Acessando o manual do comando {fb}', 6)
        print(c[6], end='')
        print(f'{help(fb)}')
        sleep(2)


ajuda()
superprint('Até logo', 1)
