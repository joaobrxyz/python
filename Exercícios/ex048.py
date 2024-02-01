soma = 0
cont = 0
for ímpar in range(1, 501, 2):
    if ímpar % 3 == 0:
        cont += 1
        soma += ímpar
print('A soma de todos os {} valores solicitados é {}'.format(cont, soma), end=' ')
