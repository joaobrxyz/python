km = float(input('Quantos km o carro rodou? '))
dia = int(input('Quantos dias que o carro foi alugado? '))
v = (dia * 60) + (km * 0.15)
print('O valor a ser pago é R${:.2f}.'.format(v))
