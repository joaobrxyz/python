def moeda(valor):
    res = str(f'R${valor:.2f}').replace('.', ',')
    return res


def metade(preço):
    return preço / 2


def dobro(preço):
    return preço * 2


def aumentar(preço, porcentagem):
    a = preço + (preço * porcentagem / 100)
    return a


def diminuir(preço, porcentagem):
    a = preço - (preço * porcentagem / 100)
    return a
