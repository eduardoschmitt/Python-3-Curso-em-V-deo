a = int(input('Digite o valor da primeira reta: '))
b = int(input('Digite o valor da segunda reta: '))
c = int(input('Digite o valor da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    if a == b and a == c:
        print('As retas formam um triângulo equilátero')
    elif a == b or a == c or b == c:
        print('As retas formam um triângulo isósceles')
    elif a!= b and a!=c and b!=c:
        print('As retas formam um triângulo escaleno')
else:
    print('As retas não formam um triângulo')