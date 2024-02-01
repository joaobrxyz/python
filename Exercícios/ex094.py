lista = list()
cont = tot = 0
while True:
    listat = dict()
    listat['nome'] = str(input('\033[1;38mNome: ')).strip()
    listat['sexo'] = ''
    while True:
        listat['sexo'] = str(input('\033[1;38mSexo [M/F]: ')).strip().upper()[0]
        if listat['sexo'] in 'MF':
            break
        else:
            print('\033[1;31mERRO! Digite apenas F ou M.')
    listat['idade'] = int(input('Idade: '))
    if listat['sexo'] in 'F':
        listat['totm'] = listat['nome']
    cont += 1
    tot += listat['idade']
    lista.append(listat.copy())
    del listat
    cnt = ''
    while True:
        cnt = str(input('\033[1;32mQuer continuar? [S/N] ')).strip().upper()[0]
        if cnt in 'SN':
            break
        else:
            print('\033[1;31mERRO! Digite apenas N ou S.')
    if cnt in 'N':
        break
média = tot / cont
print('\033[1;33m-=' * 25)
print(f'''\033[1;34m- O grupo tem {cont} pessoas.
- A média de idade é de {média:5.2f} anos.
\033[1;36m- As mulheres cadastradas foram: ''', end='')
for p in lista:
    if p['sexo'] in 'F':
        print(f'[{p["nome"]}]', end=' ')
print()
print('Lista das pessoas que estão acima da média: ')
for p in lista:
    if p['idade'] >= média:
        print(f'nome = {p["nome"]}; sexo = {p["sexo"]}; idade = {p["idade"]}.')
