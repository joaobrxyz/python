br = 'São Paulo', 'Internacional', 'Atlético-MG', 'Flamengo', 'Palmeiras', 'Grêmio', 'Fluminense', 'Corinthians', \
     'Santos', 'Ceará', 'Atlético-PR', 'Atlético-GO', 'Bragantino', 'Sport Recife', 'Vasco', 'Fortaleza', \
     'Bahia', 'Goiás', 'Coritiba', 'Botafogo'
print('\033[1;38m-=' * 45)
print(f'\033[1;34mListas de times do brasileirão: {br}.')
print('\033[1;38m-=' * 45)
print(f'\033[1;32mOs cinco primeiros colocados são: {br[0:5]}')
print('\033[1;38m-=' * 45)
print(f'\033[1;31mOs quatro últimos são: {br[-4:]}')
print('\033[1;38m-=' * 45)
print(f'\033[1;33mOs times em ordem alfábetica: {sorted(br)}')
print('\033[1;38m-=' * 45)
print('\033[1;36mO coritiba está na {}ª posição.'.format(br.index('Coritiba')+1))
print('\033[1;38m-=' * 45)
