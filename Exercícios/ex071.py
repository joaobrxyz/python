print('\033[1;33m=' * 30)
print('{:^35}'.format('\033[1;34m BANCO CEV'))
print('\033[1;33m=' * 30)
v = int(input('\033[35mQue valor você quer sacar? \033[32mR$'))
tot = v
cdl = 50
totcdl = 0
while True:
    if tot >= cdl:
        tot -= cdl
        totcdl += 1
    else:
        if totcdl > 0:
            print(f'\033[1;36mTotal de {totcdl} cédulas de R${cdl}.')
        if cdl == 50:
            cdl = 20
        elif cdl == 20:
            cdl = 10
        elif cdl == 10:
            cdl = 1
        totcdl = 0
        if tot == 0:
            break
print('\033[1;33m=' * 30)
print('\033[1;34mVolte sempre ao BANCO CEV! Tenha um bom dia!')
