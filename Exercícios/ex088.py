from random import randint
from time import sleep
lista = list()
cont = 0
print('\033[1;33m-' * 35)
print('\033[1;34m{:^35}'.format('JOGA NA MEGA SENA'))
print('\033[1;33m-' * 35)
while True:
    js = int(input('\033[35mQuantos jogos você quer que eu sorteie? '))
    print(f'\033[1;36m-=-=-=  SORTEANDO {js} JOGOS -=-=-=')
    for c in range(1, js + 1):
        while True:
            ns = randint(1, 60)
            if ns in lista:
                while ns in lista:
                    ns = randint(1, 60)
            if ns not in lista:
                lista.append(ns)
                cont += 1
            if cont == 6:
                break
        cont = 0
        lista.sort()
        sleep(1.2)
        print(f'\033[1;34mJogo {c}: {lista}')
        lista.clear()
    break
print('\033[1;32m-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')
