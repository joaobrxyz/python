frase = str(input('\033[35mDigite uma frase: ')).strip().upper()
frase1 = frase.replace(' ', '')
inverso = frase1[::-1]
'''for c in range(len(frase1) - 1, -1, -1):
    inverso += frase1[c]'''
print('\033[33mO inverso de {} é {}.'.format(frase1, inverso))
if inverso == frase1:
    print('\033[32mÉ UM PALÍNDROMO!')
else:
    print('\033[31mNÃO É UM PALÍNDROMO!')
