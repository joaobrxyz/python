print('\033[34m-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
r1 = float(input('\033[mPrimeiro segmento: '))
r2 = float(input('Segunda segmento: '))
r3 = float(input('Terceira segmento: '))
lista = [r1, r2, r3]
lista_ordenada = sorted(lista)
if lista_ordenada[2] < lista_ordenada[1] + lista_ordenada[0]:
    print('\033[32mCom esses segmentos é possível formar um triângulo!')
else:
    print('\033[31mCom esses segmentos não é possível formar um triângulo!')
print('\033[m---FIM---')
