lista = list()
while True:
    n = int(input('\033[1;35mDigite um número: '))
    lista.append(n)
    cnt = ''
    while True:
        cnt = str(input('\033[1;36mQuer continuar? [S/N] ')).upper().strip()
        if cnt in 'SN':
            break
    if cnt in 'N':
        break
lista.sort(reverse=True)
print('\033[1;38m-=' * 35)
print(f'\033[1;34mForam digitados {len(lista)} números.')
print(f'\033[1;33mA lista dos números em ordem decrescente: ', end='')
print(*lista, sep=', ')
if 5 in lista:
    print('\033[1;32mO número 5 está na lista!')
else:
    print('\033[1;31mO número 5 não faz parte da lista!')
