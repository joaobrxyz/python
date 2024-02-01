n = str(input('\033[36mDigite seu nome completo: ')).strip()
print('\033[33mExiste o sobrenome Silva nesse nome?\033[m')
print('SILVA' in n.upper())
