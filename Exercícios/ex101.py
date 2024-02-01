def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    v = ''
    if 65 > idade >= 18:
        v = '\033[1;31mVOTO OBRIGATÓRIO'
    elif idade < 18:
        v = '\033[1;32mNÃO VOTA'
    if idade >= 65 or 16 <= idade < 18:
        v = '\033[1;34mVOTO OPCIONAL'
    print(f'\033[1;36mCom {idade} anos: {v}')


# Programa principal
print('\033[1;33m-' * 30)
nasc = int(input('\033[1;35mEm que ano você nasceu? '))
voto(nasc)
