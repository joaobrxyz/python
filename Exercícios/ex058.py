from random import randint
from time import sleep
pc = randint(0, 10)
jg = 11
tentativas = 0
print('\033[1;33m-=' * 35)
print('\033[1;34mJOGO DE ADIVINHAÇÕES 2.0')
print('\033[1;33m-=' * 35)
print('\n\033[1;38mAcabei de pensar em um número entre 0 e 10. \nVocê consegue adivinhar qual foi?\n')
while jg != pc:
    jg = int(input('\033[36mQual é seu palpite: '))
    print('\033[35mPROCESSANDO...')
    sleep(1.5)
    tentativas += 1
    if jg < pc:
        print('\033[31mMais... Tente novamente!')
    if jg > pc:
        print('\033[31mMenos... Tente novamente!')
print('\033[32mVocê acertou! Você precisou de {} tentativas.'.format(tentativas))
