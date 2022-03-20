n = int(input('Digite um número: '))
if n % 2 == 0 and n != 2:
    print('Não é primo')
elif n % 3 == 0 and n != 3:
    print('Não é primo')
elif n % 5 == 0 and n != 5:
    print('Não é primo')
elif n % 7 == 0 and n != 7:
    print('Não é primo')
else:
    print('É primo')