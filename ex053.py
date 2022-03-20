f = str(input('Digite sua frase: '))
f = f.replace(' ', '')
i = f[::-1]
if i == f:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
