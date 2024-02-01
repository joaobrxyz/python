print('\033[33m-=' * 20)
print('\033[34mAnalisador de triângulos 2.0')
print('\033[33m-=' * 20)
r1 = float(input('\033[35mPrimeiro segmento: '))
r2 = float(input('Segunda segmento: '))
r3 = float(input('Terceira segmento: \033[m'))
lista = [r1, r2, r3]
lista_ordenada = sorted(lista)
if lista_ordenada[2] < lista_ordenada[1] + lista_ordenada[0]:
    print('\033[32mCom esses segmentos é possível formar um triângulo!')
else:
    print('\033[31mCom esses segmentos não é possível formar um triângulo!')
if lista_ordenada[2] < lista_ordenada[1] + lista_ordenada[0] and r1 == r2 == r3:
    print('É um triângulo equilátero, pois todos os lados são iguais.')
elif lista_ordenada[2] < lista_ordenada[1] + lista_ordenada[0] and r1 == r2 or r1 == r3 or r2 == r3:
    print('É um triângulo isósceles, pois há dois lados iguais.')
elif lista_ordenada[2] < lista_ordenada[1] + lista_ordenada[0] and r1 != r2 != r3 != r1:
    print('É um triângulo escaleno, pois todos os lados são diferentes.')
