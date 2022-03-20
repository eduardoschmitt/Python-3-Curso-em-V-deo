v = int(input('Qual valor você quer sacar? R$'))
c = int(0)
if v >= 50:
    c = v / 50
    print(f'Total de {int(c):.0f} cédula(s) de R$50,00')
    v -= (50*int(c))
if v >= 20 and v < 50:
    c = v / 20
    print(f'Total de {int(c):.0f} cédula(s) de R$20,00')
    v -= (20*int(c))
if v >= 10 and v < 20:
    c = v / 10
    print(f'Total de {int(c):.0f} cédula(s) de R$10,00')
    v -= (10*int(c))
if v >= 1 and v < 10:
    c = v / 1
    print(f'Total de {int(c):.0f} cédula(s) de R$1,00')
    v -= (1*int(c))