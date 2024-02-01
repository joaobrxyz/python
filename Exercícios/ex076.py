listagem = 'Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9
print('\033[1;33m-' * 40)
print('\033[1;34m{:^40}'.format('Listagem de preços'))
print('\033[1;33m-' * 40)
for c in range(0, len(listagem)):
    if c % 2 == 0 or c == 0:
        print('\033[1;38m{:.<30}'.format(listagem[c]), end='')
    else:
        print(f'\033[1;32mR$\033[1;38m{listagem[c]:7.2f}')
print('\033[1;33m-' * 40)
