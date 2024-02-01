from datetime import date
idade = 0
total = 0
for c in range(1, 8):
    an = int(input('\033[35mDigite o ano de nascimento da {}ª pessoa:\033[m '.format(c)))
    idade = date.today().year - an
    if idade >= 21:
        total += 1
print('{} pessoa(s) são maior(es) de idade.\nE {} pessoa(s) menor(es) de idade'.format(total, 7 - total))
