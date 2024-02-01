from time import sleep
from random import choice
print('\033[1;35m-=' * 35)
print('\033[1;34mJOGO DE JOKEMPÔ')
print('\033[1;35m-=' * 35)
jg = str(input('\033[36mDigite pedra, papel ou tesoura: ')).strip().upper()
pedra = 'PEDRA'
papel = 'PAPEL'
tesoura = 'TESOURA'
lista = [pedra, papel, tesoura]
pc = choice(lista)
print('\033[mJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
if jg == 'TESOURA' and pc == 'PEDRA':
    print('\033[31mVocê perdeu! Eu escolhi PEDRA.')
elif jg == 'TESOURA' and pc == 'PAPEL':
    print('\033[32mVocê me venceu! Eu escolhi PAPEL.')
elif jg == pc:
    print('\033[33mEmpatamos! Também escolhi {}.'.format(pc))
elif jg == 'PAPEL' and pc == 'TESOURA':
    print('\033[31mVocê perdeu! Eu escolhi TESOURA.')
elif jg == 'PAPEL' and pc == 'PEDRA':
    print('\033[32mVocê me venceu! Eu escolhi PEDRA.')
elif jg == 'PEDRA' and pc == 'PAPEL':
    print('\033[31mVocê perdeu! Eu escolhi PAPEL.')
elif jg == 'PEDRA' and pc == 'TESOURA':
    print('\033[32mVocê me venceu! Eu escolhi TESOURA.')
else:
    print('\033[31mVocê não escolheu pedra, papel ou tesoura. Tente novamente!')
