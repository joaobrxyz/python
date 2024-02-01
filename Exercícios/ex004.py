v = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(v))
print('É um número?', v.isnumeric())
print('É alfabético?', v.isalpha())
print('Só tem espaços?', v.isspace())
print('É alphanúmerico?', v.isalnum())
print('Só tem letras maiúsculas?', v.isupper())
print('Só tem letras minúsculas', v.islower())
print('Está capitalizada?', v.istitle())
# Ordem de precedência:
# 1= () Parênteses
# 2= ** Potência
# 3= * / // % Multiplicação, divisão, d inteira, resto da d.
# 4= + - Adição e subtração
