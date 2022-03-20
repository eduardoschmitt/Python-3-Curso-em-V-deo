cont = 'S'
c = 0
t5 = False
lista = []
while cont in 'Ss':
    n = int(input('Digite um número: '))
    lista.append(n)
    c += 1
    if n == 5:
        t5 = True
    cont = str(input('Deseja continuar?'))
lista.sort(reverse = True)
print(lista)
if t5 == True:
    print('Tem o número 5')
else:
    print('Não tem o número 5')
print(f'{c} números digitados')