lista = list()
while True:
    n = int(input('\033[35mDigite um número: '))
    if n in lista:
        print('\033[1;31mValor duplicado! Não vou adicionar...')
    else:
        lista.append(n)
        print('\033[1;32mValor adicionado com sucesso...')
    cnt = ''
    while True:
        cnt = str(input('\033[1;33mQuer continuar? [S/N] ')).strip().upper()
        if cnt in 'SN':
            break
    if cnt in 'N':
        break
print('\033[1;36m=-' * 30)
print('\033[1;34mVocê digitou os valores: ', end='')
lista.sort()
print(*lista, sep=', ')
