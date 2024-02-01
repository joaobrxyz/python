print('\033[1;34m-' * 25)
print('\033[1;36mSEQUÊNCIA DE FIBONACCI')
print('\033[1;34m-' * 25)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
t3 = t1 + t2
cont = 3
print('{} → {} → {}'.format(t1, t2, t3), end='')
if n > 3:
    while cont < n:
        t1 = t2
        t2 = t3
        t3 = t1 + t2
        print(' → {}'.format(t3), end='')
        cont += 1
print(' FIM')
