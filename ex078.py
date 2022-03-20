lista = []
for c in range(5):
    num = int(input(f'Digite o {c+1}º valor: '))
    lista.append(num)
print(lista)
print(f'o maior valor foi {max(lista)} na posição {lista.index(max(lista))}')
print(f'o menor valor foi {min(lista)} na posição {lista.index(min(lista))}')