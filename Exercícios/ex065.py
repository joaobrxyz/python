tot = 0
cont = 0
maior = 0
menor = 0
r = ''
while r in 'S':
    n = int(input('\033[35mDigite um número: '))
    r = input('\033[33mQuer continuar? [S/N] ').strip().upper()
    cont += 1
    tot += n
    if cont == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
média = tot / cont
print('\033[34mVocê digitou {} números e a média entre todos os números é {} \n\033[32mO maior foi {}\033[31m e o menor foi {}.'.format(cont, média, maior, menor))
