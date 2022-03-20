n1 = int(input("Digite o primeiro número: "))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'{n1} é maior que {n2}')
elif n2 > n1:
    print(f'{n2} é maior que {n1}')
elif n1 == n2:
    print(f'{n1} e {n2} são iguais')
else:
    print('ERROR 404')