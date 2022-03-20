a = int(input('Digite o valor da primeira reta: '))
b = int(input('Digite o valor da segunda reta: '))
c = int(input('Digite o valor da terceira reta: '))
if a < b + c and b < a + c and c < a + b:
    print('As retas formam um triângulo')
else:
    print('As retas não formam um triângulo')