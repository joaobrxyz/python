def ficha(nome='<desconhecido>', gols="0"):
    if nome == '' and gols.isnumeric():
        print(f'\033[1;34mO jogador <desconhecido> fez {gols} gol(s) no campeonato.')
    elif not gols.isnumeric() and nome != '':
        print(f'\033[1;34mO jogador {nome} fez 0 gol(s) no campeonato.')
    elif nome == '' and not gols.isnumeric():
        print(f'\033[1;34mO jogador <desconhecido> fez 0 gol(s) no campeonato.')
    elif nome != '' and gols.isnumeric():
        print(f'\033[1;34mO jogador {nome} fez {gols} gol(s) no campeonato.')


# Programa principal
print('\033[1;33m-' * 30)
jg = str(input('\033[1;38mNome do jogador: '))
g = input('Número de gols: ')
ficha(jg, g)
