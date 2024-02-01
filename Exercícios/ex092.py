from datetime import date
dict = dict()
dict['nome'] = str(input('\033[1;38mNome: '))
dict['id'] = date.today().year - int(input('Ano de nascimento: '))
dict['ctps'] = int(input('Carteira de trabalho (0 não tem): '))
if dict['ctps'] > 0:
    dict['anocont'] = int(input('Ano de contratação: '))
    dict['salário'] = float(input('Salário: R$'))
print(f'\033[1;34mO nome é {dict["nome"]}.')
print(f'O/A {dict["nome"]} tem {dict["id"]} anos.')
print(f'CTPS é {dict["ctps"]}.')
if dict['ctps'] > 0:
    print(f'\033[1;36m    - A contratação foi em {dict["anocont"]}.')
    print(f'    - O salário tem o valor de R${dict["salário"]:.2f}.')
    print(f'    - A aposentadoria vai ser com {dict["anocont"] + 35 - (date.today().year - dict["id"])} anos.')
