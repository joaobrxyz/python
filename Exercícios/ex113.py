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


def leiafloat(mensagem):
    while True:
        num = input(mensagem).strip()
        num1 = num.replace('.', '')
        if KeyboardInterrupt and num == '':
            print('\033[1;31mO usuário preferiu não informar os dados!\033[m')
            return 0
        elif not num1.isnumeric():
            print('\033[1;31mErro! Digite um número real válido.\033[m')
        else:
            return float(num)


ni = leiaint('Digite um número inteiro: ')
nr = leiafloat('Digite um número real: ')
print(f'O valor inteiro digitado foi {ni} e o real foi {nr}.')
