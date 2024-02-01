def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')


def metade(preço, reais=False):
    if reais:
        return f'R${preço / 2:.2f}'.replace('.', ',')
    else:
        return preço / 2


def dobro(preço, reais=False):
    if reais:
        return f'R${preço * 2:.2f}'.replace('.', ',')
    else:
        return preço * 2


def aumentar(preço, porcentagem, reais=False):
    a = preço + (preço * porcentagem / 100)
    if reais:
        return f'R${a:.2f}'.replace('.', ',')
    else:
        return a


def diminuir(preço, porcentagem, reais=False):
    a = preço - (preço * porcentagem / 100)
    if reais:
        return f'R${a:.2f}'.replace('.', ',')
    else:
        return a


def resumo(preço, p_aumento, p_redução):
    print('\033[1;33m-' * 30)
    print(f'\033[1;34m{"RESUMO DO VALOR":^30}')
    print('\033[1;33m-' * 30)
    print(f'\033[1;36mPreço analizado:    R${preço:.2f}'.replace('.', ','))
    print(f'\033[1;32mDobro do preço:     R${dobro(preço):.2f}'.replace('.', ','))
    print(f'\033[1;31mMetade do preço:    R${metade(preço):.2f}'.replace('.', ','))
    print(f'\033[1;32m{p_aumento}% de aumento:     R${aumentar(preço, p_aumento):.2f}'.replace('.', ','))
    print(f'\033[1;31m{p_redução}% de redução:     R${diminuir(preço, p_redução):.2f}'.replace('.', ','))
    print('\033[1;33m-' * 30)
