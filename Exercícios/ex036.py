print('\033[33m-=' * 25)
print('\033[34mFinanciamento de imóveis')
print('\033[33m-=' * 25)
vcasa = float(input('\033[mDigite o valor da casa: R$'))
sal = float(input('Digite o salário do comprador: R$'))
pg = int(input('Em quantos anos você irá pagar: '))
pgd = vcasa / (pg * 12)
sald = sal * 30 / 100
if sald < pgd:
    print('\033[31mVocê não comprar essa casa, pois as parcelas ultrapassam 30% do salário.')
else:
    print('\033[32mVocê poderá comprar está casa! O valor das parcelas é R${:.2f}'.format(pgd))
