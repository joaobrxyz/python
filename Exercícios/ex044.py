p = float(input('\033[35mDigite o valor dos compras:\033[m R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = p - (p * 10 / 100)
    print('À vista \033[34mdinheiro/cheque:\033[m R${:.2f} '.format(p - (p * 10 / 100)))
elif opção == 2:
    total = p - (p * 5 / 100)
    print('À vista no \033[34mcartão\033[m: R${:.2f}'.format(p - (p * 5 / 100)))
elif opção == 3:
    total = p
    print('\033[34m2x no cartão:\033[m R${:>2f} por mês SEM JUROS'.format(p/2))
elif opção == 4:
    total = (p + (p * 20 / 100))
    vezes = int(input('Em quantas vezes? '))
    print('\033[34m{}x no cartão:\033[m R${:.2f} por mês COM JUROS.'.format(vezes, (p + (p * 20 / 100)) / vezes))
else:
    total = p
    print('Opção INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(p, total))
