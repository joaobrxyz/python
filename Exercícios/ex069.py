p18 = hm = m20 = 0
while True:
    print('\033[1;33m-' * 18)
    print('\033[1;34mCadastre uma pessoa: ')
    print('\033[1;33m-' * 18)
    i = int(input('\033[35mIdade: '))
    if i >= 18:
        p18 += 1
    s = ' '
    while not s in 'MF':
        s = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if s in 'M':
        hm += 1
    if i < 20 and s in 'F':
        m20 += 1
    sn = ' '
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if sn in 'N':
        break
print('\033[1;36m====== FIM DO PROGRAMA ======')
print(f'\033[1;38mTotal de pessoas com mais de 18: {p18}.')
print(f'Ao todos temos {hm} homens cadastrados.')
print(f'E temos {m20} mulheres com menos de 20 anos.')
