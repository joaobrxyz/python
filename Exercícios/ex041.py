from datetime import date
print('\033[33m-='* 35)
print('\033[34mCategorias da confederação nacional de natação')
print('\033[33m-='* 35)
dn = int(input('\033[mDigite o ano de nascimento do atleta: '))
idade = date.today().year - dn
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif 9 < idade <= 14:
    print('Sua categoria é INFANTIL')
elif 14 < idade <= 19:
    print('Sua categoria é JUNIOR.')
elif idade <= 25:
    print('Sua categoria é SÊNIOR.')
elif idade > 25:
    print('Sua categoria é MASTER.')
