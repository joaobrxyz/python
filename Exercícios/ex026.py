frase = str(input('Digite uma frase: ')).strip()
la = frase.upper().count('A')
lpv = frase.upper().find('A') + 1
lpa = frase.upper().rfind('A') + 1
print('\033[33mQuantidades de A: {} \n\033[34mPosição do primeiro A: {} \n\033[36mPosição do último A: {}'.format(la, lpv, lpa))
