from random import choice
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo: ')
a3 = input('Digite o nome do terceiro: ')
a4 = input('Digite o nome do quarto: ')
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O sorteado para apagar o quadro foi {}.'.format(escolhido))
