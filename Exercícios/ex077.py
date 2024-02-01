palavras = 'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro'
for p in palavras:
    print(f'\n\033[1;34mNa palavra {p.upper()} temos:\033[1;32m', end=' ')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
