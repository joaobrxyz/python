dado = list()
maiorp = menorp = 0
temp = list()
while True:
    temp.append(str(input('\033[1;35mNome: ')))
    temp.append(float(input('Peso: ')))
    if len(dado) == 0:
        maiorp = menorp = temp[1]
    else:
        if temp[1] > maiorp:
            maiorp = temp[1]
        if temp[1] < menorp:
            menorp = temp[1]
    dado.append(temp[:])
    temp.clear()
    resp = ''
    while True:
        resp = str(input('\033[1;32mQuer continuar? [S/N] ')).strip().upper()
        if resp in 'SN':
            break
    if resp in 'N':
        break
print('\033[1;38m-=' * 35)
print(f'\033[1;34mAo todo, você cadastrou {len(dado)} pessoas.')
print(f'\033[1;33mO maior peso foi de {maiorp}Kg. Peso de ', end='')
for p in dado:
    if p[1] == maiorp:
        print(f'[{p[0]}]', end='')
print(f'\n\033[1;36mO menor peso foi de {menorp}Kg. Peso de ', end='')
for p in dado:
    if p[1] == menorp:
        print(f'[{p[0]}]', end=' ')
