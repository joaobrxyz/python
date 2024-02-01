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
