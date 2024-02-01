somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    print('\033[36m---- {}º pessoa -----'.format(c))
    nome = str(input('\033[35mDigite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (F/M): ')).strip()
    somaidade += idade
    if c == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
médiaidade = somaidade / 4
print('\033[34mA média de idade do grupo é de {} anos'.format(médiaidade))
print('O nome do homem mais velho é {} ele tem {} anos.'.format(nomevelho, maioridadehomem))
print('Ao todo são {} mulher(es) com menos de 20 anos.'.format(totmulher20))
