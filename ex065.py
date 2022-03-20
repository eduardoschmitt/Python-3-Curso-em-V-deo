i = int(1)
c = media = maior = int(0)
menor = int(9*99)
while i == 1:
    n = int(input('Digite um número: '))
    c += 1
    media += n
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    i = int(input('''Deseja continuar?
    [1] - SIM
    [0] - NÃO
    R: '''))
print(f'A media dos valores foi {media/c}! ')
print(f'O menor e maior termo são respectivamente {menor} e {maior}')