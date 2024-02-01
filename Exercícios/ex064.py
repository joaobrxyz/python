n = cont = soma = 0
while n != 999:
    n = int(input('\033[35mDigite um número [999 para parar]: '))
    if n != 999:
        soma += n
        cont += 1
print('\033[32mVocê digitou {} números e a soma entre eles é {}.'.format(cont, soma))
