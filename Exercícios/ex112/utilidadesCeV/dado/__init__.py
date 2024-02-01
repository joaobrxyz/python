def leiadinheiro(msg):
    while True:
        valor = str(input(msg)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print(f'\033[1;31mERRO: "{valor}" é um preço inválido!\033[m')
        else:
            real = float(valor)
            return real


def leiaint(mensagem):
    num = input(mensagem)
    while not num.isnumeric():
        print('\033[1;31mErro! Digite um número inteiro válido.\033[m')
        num = input(mensagem)
    return num
