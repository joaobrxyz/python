n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro: '))
n3 = float(input('Digite mais um: '))
if n1 > n2 and n1 > n3:
    print('\033[32mO maior número é {:.0f}'.format(n1))
if n2 > n1 and n2 > n3:
    print('\033[32mO maior número é {:.0f}'.format(n2))
if n3 > n1 and n3 > n2:
    print('\033[32mO maior número é {:.0f}\033[m'.format(n3))
if n1 < n2 and n1 < n3:
    print('\033[31mO menor número é {:.0f}'.format(n1))
if n2 < n1 and n2 < n3:
    print('\033[31mO menor número é {:.0f}'.format(n2))
if n3 < n1 and n3 < n2:
    print('\033[31mO menor número é {:.0f}\033[m'.format(n3))
