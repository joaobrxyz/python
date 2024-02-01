pr = int(input('Primeiro termo: '))
razão = int(input('Digite a razão: '))
total = pr + (10 - 1) * razão
for pa in range(pr, total + razão, razão):
    print(pa, end=' -> ')
print('ACABOU')
