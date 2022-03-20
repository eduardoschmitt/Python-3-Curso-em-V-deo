bi = ''
n = int(input('Escreva um número inteiro qualquer: '))
print('1 para binário')
print('2 para octal')
print('3 para hexadecimal')
base = int(input('Escolha a base para a conversão: '))

if base == 1:
    while n > 0:
        t = n % 2
        t = str(t)
        bi = t + bi
        n = n / 2
        n = int(n)

elif base == 2:
    while n > 0:
        t = n % 8
        t = str(t)
        bi = t + bi
        n = n / 8
        n = int(n)

elif base == 3:
    while n > 0:
        t = n % 16
        if t == 10:
            bi = 'A' + bi
            n = n / 16
            n = int(n)
        elif t == 11:
            bi = 'B' + bi
            n = n / 16
            n = int(n)
        elif t == 12:
            bi = 'C' + bi
            n = n / 16
            n = int(n)
        elif t == 13:
            bi = 'D' + bi
            n = n / 16
            n = int(n)
        elif t == 14:
            bi = 'E' + bi
            n = n / 16
            n = int(n)
        elif t == 15:
            bo = 'F' + bi
            n = n / 16
            n = int(n)
        else:
            t = str(t)
            bi = t + bi
            n = n / 16
            n = int(n)

else:
    print('Número da base inválido')
print(bi)