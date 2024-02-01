lista = list()
tot = totg = 0
while True:
    dict = dict()
    dict['nome'] = str(input('\033[1;38mNome do jogador: ')).strip()
    partidas = int(input(f'Quantas partidas {dict["nome"]} jogou? '))
    if partidas > 0:
        dict['gols'] = list()
        for p in range(1, partidas+1):
            qp = int(input(f'\033[1;35mQuantos gols na {p}º partida? '))
            dict['gols'].append(qp)
            tot += qp
            del qp
    lista.append(dict.copy())
    del dict
    cnt = ''
    while True:
        cnt = str(input('\033[1;32mQuer continuar [S/N]: ')).strip().upper()[0]
        if cnt in 'SN':
            break
        print('\033[1;31mERRO! Digite apenas N ou S.')
    if cnt in 'N':
        break
print(f'\033[1;38m{"cod":>}{"nome":>7}      {"gols":>10}     {"total":>15}')
print(f'\033[1;33m-'*55)
for i, j in enumerate(lista):
    for g in j['gols']:
        totg = 0
        totg += g
    print(f'\033[1;34m{i+1:^3}   {str(j["nome"]):^4}           {str(j["gols"])}           {totg:4}')
    del totg
while True:
    dados = int(input('\033[1;35mMostrar dados de qual jogador? (999 para parar) '))
    if dados == 999:
        break
    if dados > len(lista) or dados < 1:
        print(f'\033[1;31mERRO! Não existe jogador com código {dados}! Tente novamente.')
    else:
        print(f'\033[1;38m-- LEVANTAMENTO DO JOGADOR {lista[dados-1]["nome"]}:')
        for i, gol in enumerate(lista[dados-1]['gols']):
            print(f'\033[1;36mNo jogo {i+1} fez {gol} gols.')
        print('\033[1;38m-'*30)
print('\033[1;32m< VOLTE SEMPRE >')
