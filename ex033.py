n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if n1 > n2 and n1 > n3:
    print(f'O número {n1} é o maior')
if n2 > n1 and n2 > n3:
    print(f'O número {n2} é o maior')
if n3 > n1 and n3 > n2:
    print(f'O número {n3} é o maior')

if n1 < n2 and n1 < n3:
    print(f'O número {n1} é o menor')
if n2 < n1 and n2 < n3:
    print(f'O número {n2} é o menor')
if n3 < n1 and n3 < n2:
    print(f'O número {n3} é o menorr')