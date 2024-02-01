car = float(input('Digite a velocidade atual do carro: '))
if car > 80:
    print('\033[31mVocê foi multado por R${:.2f} por ter ultrapassado 80KM/h.'.format((car - 80) * 7))
else:
    print('\033[32mVocê está dentro do limite de velocidade.')
