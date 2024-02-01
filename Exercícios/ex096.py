def área():
    print('\033[1;33mControle de terrenos')
    print('\033[1;38m-'*30)
    larg = float(input('\033[1;36mLargura (m): '))
    compr = float(input('Comprimento (m): '))
    área0 = larg * compr
    print(f'\033[1;34mA área de um terreno {larg}x{compr} é de {área0}m².')


área()
