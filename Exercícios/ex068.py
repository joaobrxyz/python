from random import randint
cont = 0
print('\033[1;33m=-' * 25)
print('\033[1;34mVAMOS JOGAR PAR OU ÍMPAR')
while True:
    print('\033[33m=-' * 25)
    v = int(input('\033[35mDigite um valor: '))
    pi = str(input('Par ou ímpar? [P/I] ')).strip().upper()
    pc = randint(1, 10)
    r = v + pc
    if pi in 'P':
        if r % 2 == 0:
            print('\033[1;38m-' * 35)
            print(f'\033[36mVocê jogou {v} e o computador {pc}. Total de {r} DEU PAR!')
            print('\033[1;38m-' * 35)
            print('\033[32mVOCÊ VENCEU!')
        if r % 2 != 0:
            print('\033[1;38m-' * 35)
            print(f'\033[36mVocê jogou {v} e o computador {pc}. Total de {r} DEU ÍMPAR!')
            print('\033[1;38m-' * 35)
            print('\033[32mVOCÊ PERDEU!')
            break
    if pi in 'I':
        if r % 2 != 0:
            print('\033[1;38m-' * 35)
            print(f'\033[36mVocê jogou {v} e o computador {pc}. Total de {r} DEU ÍMPAR!')
            print('\033[1;38m-' * 35)
            print('\033[1;32mVOCÊ GANHOU')
        if r % 2 == 0:
            print('\033[1;38m-' * 35)
            print(f'\033[36mVocê jogou {v} e o computador {pc}. Total de {r} DEU PAR!')
            print('\033[1;38m-' * 35)
            print('\033[1;32mVOCÊ PERDEU!')
            break
    print('\033[1;32mVamos continuar...')
    cont += 1
print(f'\033[1;38mGAME OVER! Você venceu {cont} vezes.')
