sit = dict()
sit['nome'] = str(input('\033[35mNome: '))
sit['média'] = float(input(f'Média de {sit["nome"]}: '))
if sit['média'] >= 7:
    sit['situ'] = '\033[1;32mAprovado'
elif sit['média'] >= 5:
    sit['situ'] = '\033[1;33mRecuperação'
else:
    sit['situ'] = '\033[1;31mReprovado'
print(f'\033[1;33m-'*30)
print(f'\033[1;34mNome é igual a {sit["nome"]}.')
print(f'\033[1;36mMédia é igual a {sit["média"]}')
print(f'\033[1;38mSituação é igual a {sit["situ"]}.')
