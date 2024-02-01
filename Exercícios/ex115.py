from ex115.lib.interface import *
from ex115.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
while True:
    resp = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoas', 'Sair do Sistema'])
    if resp == 1:
        # Opção 1 de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif resp == 2:
        # Opção de cadastrar uma nova pessoa.
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho('\033[mSaindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida')
    sleep(2)
