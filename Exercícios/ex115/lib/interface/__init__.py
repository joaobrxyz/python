def leiaint(mensagem):
    while True:
        num = input(mensagem).strip()
        if KeyboardInterrupt and num == '':
            print('\033[1;31mO usuário preferiu não informar os dados!\033[m')
            return 0
        elif not num.isnumeric():
            print('\033[1;31mErro! Digite um número inteiro válido.\033[m')
        else:
            return int(num)


def linha(tam=42):
    return '\033[1;38m-' * tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabeçalho('\033[36mMENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[33m{c} - \033[34m{i}')
        c += 1
    print(linha())
    opc = leiaint('\033[32mSua opção: ')
    return opc
