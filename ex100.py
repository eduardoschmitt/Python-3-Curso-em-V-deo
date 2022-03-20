from random import randint

def sorteia(lista):
    print('')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
    print(lista)

def somaPar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    print(soma)

numeros = list()
sorteia(numeros)
somaPar(numeros)