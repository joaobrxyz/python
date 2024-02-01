num0a20 = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', \
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'
cnt = ''
while True:
    num = int(input('\033[35mDigite um número de 0 à 20: '))
    if num > 20 or num < 0:
        print('Tente novamente. ', end='')
    else:
        print(f'\033[1;34mVocê digitou o número {num0a20[num]}.')
        while True:
            cnt = str(input('\033[1;35mVocê quer continuar? [S/N] ')).strip().upper()
            if cnt in 'SN':
                break
        if cnt in 'N':
            break
print('\033[1;34mPrograma finalizado!')
