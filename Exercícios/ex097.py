def escreva(str):
    cnt = len(str) + 4
    print('\033[1;33m~' * cnt)
    print(f'\033[1;34m  {str}')
    print('\033[1;33m~' * cnt)


escreva('João Vitor')
escreva('Curso de Python no Youtube')
escreva('CeV')
