print('\033[33m-=' * 25)
print('\033[34mCalculadora do IMC')
print('\033[33m-=' * 25)
peso = float(input('\033[35mDigite o seu peso: (Kg) '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura**2
if imc < 18.5:
    print('\033[36mVocê está abaixo do peso ideal.')
elif 18.5 < imc < 25:
    print('\033[32mVocê está no peso ideal.')
elif 25 < imc < 30:
    print('\033[36mVocê está sobrepeso.')
elif 30 < imc < 40:
    print('\033[31mVocê está na obesidade.')
elif imc > 40:
    print('\033[31mVocê está na obesidade mórbida, cuidado.')
