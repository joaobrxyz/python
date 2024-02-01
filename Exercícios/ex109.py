from ex109 import moeda
p = float(input('\033[1;36mDigite o preço: R$'))
print(f'\033[1;33mA metade de {moeda.moeda(p)} é {moeda.metade(p, reais=True)}')
print(f'\033[1;34mO dobro de {moeda.moeda(p)} é {moeda.dobro(p, reais=True)}')
print(f'\033[1;32mAumentando 10%, temos {moeda.aumentar(p, 10, reais=True)}')
print(f'\033[1;31mReduzindo 13%,temos {moeda.diminuir(p, 13, reais=True)}')
