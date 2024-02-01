d = float(input('Digite a distância percorrigada em km na viagem: '))
if d <= 200:
    print('O preço da passagem é \033[31mR${:.2f}'.format(d * 0.5))
else:
    print('O valor da passagem é \033[31mR${:.2f}'.format(d * 0.45))
print('\033[m---FIM---')
