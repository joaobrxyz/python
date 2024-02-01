n = str(input('Digite seu nome completo: ')).strip()
dividido = n.split()
print('\033[34mPrimeiro nome: {} \n\033[33mÚltimo nome: {}'.format(dividido[0], dividido[len(dividido)-1]))
