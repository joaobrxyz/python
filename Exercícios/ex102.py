def fatorial(n, show=False):
    """
    → Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor fatorial de um número n.
    """
    ng = 1
    for c in range(n, 0, -1):
        ng *= c
        if show:
            print(f'{c}', end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    print(ng)
    return ng


# Programa principal
fatorial(5, show=True)
help(fatorial)
