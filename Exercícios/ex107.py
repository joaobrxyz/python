from ex107 import moeda
p = float(input('\033[1;36mDigite o preço: R$'))
print(f'\033[1;33mA metade de {p} é {moeda.metade(p)}')
print(f'\033[1;34mO dobro de {p} é {moeda.dobro(p)}')
print(f'\033[1;32mAumentando 10%, temos {moeda.aumentar(p, 10)}')
print(f'\033[1;31mReduzindo 13%,temos {moeda.diminuir(p, 13)}')
