from ex108 import moeda
p = float(input('\033[1;36mDigite o preço: R$'))
print(f'\033[1;33mA metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'\033[1;34mO dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'\033[1;32mAumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'\033[1;31mReduzindo 13%,temos {moeda.moeda(moeda.diminuir(p, 13))}')
