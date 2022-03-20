fatorial = int(1)
resposta = str('')
n = int(input('Escreva um número: '))
for c in range(1, n+1):
    fatorial *= c
    if c != 1:
        resposta = f'{c} X ' + resposta
print(f'{n}! = {resposta}1 = {fatorial}')