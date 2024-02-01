listaalu = []
listat = []
cont = 0
while True:
    listat.append(str(input('\033[1;35mNome: ')))
    listat.append(float(input('Nota 1: ')))
    listat.append(float(input('Nota 2: ')))
    listat.append((listat[1] + listat[2]) / 2)
    listaalu.append(listat[:])
    listat.clear()
    sn = ''
    while True:
        sn = str(input('\033[1;32mQuer continuar? [S/N] ')).strip().upper()
        if sn in 'SN':
            break
    if sn in 'N':
        break
print('-=' * 35)
print(f'\033[1;34m{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('\033[1;33m----------------------')
for i, a in enumerate(listaalu):
    print(f'{i+1:<4}{a[0]:<10}{a[2]:>8.1f}')
while cont != 999:
    cont = int(input('\033[1;36mMostrar notas de qual aluno? (999 interrompe): '))
    print(f'As notas do(a) {listaalu[cont-1][0]}{listaalu[cont-1][1:3]}')
