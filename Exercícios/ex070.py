tg = p1000 = nb = vb = c = 0
print('\033[1;33m-' * 25)
print('\033[1;34m   LOJA SUPER BARATÃO')
print('\033[1;33m-' * 25)
while True:
    n = str(input('\033[35mNome do produto: '))
    v = float(input('Valor do produto: \033[32mR$'))
    tg += v
    if v > 1000:
        p1000 += 1
    c += 1
    if c == 1 or v < vb:
        nb = n
        vb = v
    cnt = ' '
    while cnt not in 'SN':
        cnt = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if cnt == 'N':
        break
print('\033[1;38m------- FIM DO PROGRAMA -------')
print(f'\033[1;36mO total da compra foi R${tg:.2f}.')
print(f'Temos {p1000} produtos custando mais de R$1000.')
print(f'O produto mais barato foi {nb} custando R${vb:.2f}')
