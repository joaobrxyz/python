sal = float(input('Digite o salário: R$'))
if sal>= 1250:
    print('O novo salário é R${}{:.2f}{} com o aumento de 10%.'.format('\033[32m', (sal * 10 / 100) + sal, '\033[m'))
else:
    print('O novo salário e R${}{:.2f}{} com o aumento de 15%.'.format('\033[32m', (sal * 15 / 100) + sal, '\033[m'))
print('---FIM---')
