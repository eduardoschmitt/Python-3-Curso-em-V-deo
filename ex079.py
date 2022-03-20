lista = []
while True:
    num = int(input('Digite um número: '))
    if num == 0:
        break
    elif not num in lista:
        lista.append(num)
    else:
        print('Número já existente na lista')
lista.sort()
print(lista)