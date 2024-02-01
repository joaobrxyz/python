n = int(input('Digite um número: '))
if n % 2 == 0:
    print('\033[33mO número é par.')
else:
    print('\033[36mO número é ímpar.')
print('\033[m---FIM---')
