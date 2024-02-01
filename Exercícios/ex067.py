while True:
    n = int(input('\033[35mDigite um número para ver a tabuada: '))
    if 0 < n:
        print('\033[33m-' * 30)
        for c in range(1, 11):
            print(f'\033[34m{n} x {c} = {n * c}')
        print('\033[33m-' * 30)
    else:
        break
print('\033[31mPROGRAMA DE TABUADA ENCERRADO. \033[32mVolte sempre!')
