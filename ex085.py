lista = [[],[]]
c = 1
while c != 8:
    n = int(input(f'Digite o {c} número: '))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
    c += 1
lista[0].sort()
lista[1].sort()
print(f'Os impares foram {lista[1]}')
print(f'Os pares foram {lista[0]}')
