from datetime import date
dn = int(input('\033[33mDigite o ano que você nasceu: '))
a = date.today().year - dn
if a < 18:
    print('\033[34mAinda não é a hora de se alistar, espere {} ano(s).'.format(18 - a))
elif a > 18:
    print('\033[31mJá passou da hora de se alistar, era pra ter se alistado há {} ano(s).'.format(a - 18))
else:
    print('\033[32mEssa é a hora de se alistar, verifique a data limite de apresentação no site: https://www.eb.mil.br/web/ingresso/servico-militar.')
