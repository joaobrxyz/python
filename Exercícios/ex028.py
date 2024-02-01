from random import randint
from time import sleep
na = randint(0, 5)
print('\033[1;33m-=' * 50)
print('\033[1;36mVou pensar em um número entre 0 a 5. Tente adivinhar...')
print('\033[1;33m-=' * 50)
ne = int(input('\033[mEm qual número eu pensei? '))
print('\033[1;35mPROCESSANDO...\033[m')
sleep(3)
if na == ne:
    print('\033[32mParábens, você me venceu!')
else:
    print('\033[31mGanhei! Eu pensei no número {} e não no {}!'.format(na, ne))
