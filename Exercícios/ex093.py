dict = dict()
tot = 0
dict['nome'] = str(input('\033[1;38mNome do jogador: ')).strip()
partidas = int(input(f'Quantas partidas {dict["nome"]} jogou? '))
if partidas > 0:
    dict['gols'] = list()
    for p in range(1, partidas+1):
        qp = int(input(f'\033[1;35m   Quantos gols na {p}º partida? '))
        dict['gols'].append(qp)
        tot += qp
        del qp
print(f'\033[1;34mO jogador {dict["nome"]} jogou {partidas} partidas.')
for p in range(1, partidas + 1):
    print(f'\033[1;36m   => Na {p}º partida, fez {dict["gols"][p-1]}')
print(f'\033[1;32mFoi no total de {tot} gols.')
