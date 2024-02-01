num = int(input('Digite um número para ver a tabuada: '))
for c in range(1, 11):
    print('{} x {:2} = {:3}'.format(num, c, num * c))
