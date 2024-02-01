from random import randint
from time import sleep
from operator import itemgetter
dado = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6), 'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
print('\033[1;33mValores sorteados:')
for k, v in dado.items():
    print(f'\033[1;38m{k} tirou {v} no dado.')
    sleep(1.6)
ranking = sorted(dado.items(), key=itemgetter(1), reverse=True)
print('\033[1;33m-=' * 30)
print('\033[1;34m  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    \033[1;36m{i+1}° lugar: {v[0]} com {v[1]}.')
    sleep(1.6)
