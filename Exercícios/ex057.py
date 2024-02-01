s = str(input('\033[35mDigite seu sexo: [M/F] ')).strip().upper()[0]
if s != 'F' 'M':
    while s not in 'F' 'M':
        s = str(input('\033[31mDado inválido. Por favor, digite seu sexo: ')).strip().upper()[0]
print('\033[32mSexo {} registrado com sucesso.'.format(s))
