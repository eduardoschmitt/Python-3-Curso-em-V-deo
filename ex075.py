num = (int(input()), int(input()), int(input()), int(input()))
print(f'Você digitou os valores {num}')
print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valores pares digitados são: ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')