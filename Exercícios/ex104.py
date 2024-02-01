def leiaint(mensagem):
    num = input(mensagem)
    while not num.isnumeric():
        print('\033[1;31mErro! Digite um número inteiro válido.\033[m')
        num = input(mensagem)
    return num


# Programa principal
n = leiaint('\033[1;38mDigite um número: ')
print(f'\033[1;34mVocê acabou de digitar o número {n}.')
