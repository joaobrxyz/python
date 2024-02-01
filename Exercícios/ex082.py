listac = list()
listap = list()
listai = list()
while True:
    num = int(input('\033[1;35mDigite um número: '))
    listac.append(num)
    if num % 2 == 0:
        listap.append(num)
    else:
        listai.append(num)
    cnt = ''
    while True:
        cnt = str(input('Quer continuar? [S/N] ')).strip().upper()
        if cnt in 'SN':
            break
    if cnt in 'N':
        break
print('\033[1;38m=-' * 35)
print(f'\033[1;34mA lista completa é: ', end='')
print(*listac, sep=", ")
print('\033[1;33mA lista de pares é: ', end='')
print(*listap, sep=', ')
print('\033[1;36mA lista de ímpares é: ', end='')
print(*listai, sep=', ')
