from math import radians, tan, cos, sin
a = float(input('Digite o valor do ângulo: '))
seno = sin(radians(a))
cosseno = cos(radians(a))
tangente = tan(radians(a))
print('O ângulo de {} tem o seno de {:.2f}.'.format(a, seno))
print('O ângulo de {} tem o cosseno de {:.2f}'.format(a, cosseno))
print('O ângulo de {} tem a tangente de {:.2f}'.format(a, tangente))
