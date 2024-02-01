from datetime import date
ano = int(input('Qual ano você quer analizar? Digite 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {}{}{} é bissexto!'.format('\033[34m', ano, '\033[m'))
else:
    print('O ano {}{}{} não é bissexto!'.format('\033[31m', ano, '\033[m'))
print('---FIM---')
