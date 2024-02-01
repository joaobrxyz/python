from time import sleep
n1 = 0
n2 = 0
r = 4
while r != 5:
    if r == 4:
        n1 = int(input('\033[35mDigite um valor: '))
        n2 = int(input('Digite outro valor: '))
    print('\033[1;34m-=' * 25)
    sleep(1.5)
    r = int(input('''\033[1;36m     [ 1 ] somar
     [ 2 ] multiplicar
     [ 3 ] maior
     [ 4 ] outros números
     [ 5 ] sair do programa
  \033[1;38m>>>>> Qual é sua opção? '''))
    if r > 5 or r == 0:
        print('\033[31mOpção inválida. Tente novamente!')
    m = 0
    if n1 > n2:
        m = n1
    elif n2 > n1:
        m = n2
    else:
        m = n1
    if r == 1:
        print('\033[33m\nO resultado da soma entre {} + {} = {}.\n'.format(n1, n2, n1 + n2))
    elif r == 2:
        print('\033[33m\nO resultado da multiplicação entre {} x {} = {}.\n'.format(n1, n2, n1 * n2))
    elif r == 3:
        print('\033[33m\nO maior número é {}\n'.format(m))
print('\033[1;38mFinalizando..')
sleep(2.5)
print('\033[1;33m-=' * 20)
print('\033[1;32mFim do programa! Volte sempre!')
