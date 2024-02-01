n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1 + n2) / 2
if m < 5:
    print('\033[31mO aluno foi REPROVADO! A média foi {:.1f}.'.format(m))
elif 5 <= m <= 6.9:
    print('\033[33mO aluno ficou de RECUPERAÇÃO. A média foi {:.1f}.'.format(m))
elif m >= 7:
    print('\033[32mParábens! O aluno foi APROVADO. Á média foi {:.1f}'.format(m))
