n = 1
lista = []
par = []
impar = []
while n != 0:
    n = int(input('Digite um número ou 0 para parar: '))
    if n != 0: lista.append(n)
for c in lista:
    if c % 2 == 0:
        par.append(c)
    else:
        impar.append(c)
print(f'sua lista foi {lista}')
print(f'os números pares são {par}')
print(f'os impares são {impar}')
