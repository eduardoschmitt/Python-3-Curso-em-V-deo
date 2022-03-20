from math import hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
r = ((co * co) + (ca * ca)) ** (1/2)
hi = hypot(co,ca)
print(f'O comprimento da hipotenusa é {r:.2f}')
print(f'O comprimento da hipotenusa é {hi:.2f}')