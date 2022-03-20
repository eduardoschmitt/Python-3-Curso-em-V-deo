q = float(input('Qual a quantidade de Km percorridos? '))
d = int(input('Qual a quantidade de dia? '))
p = (q * 0.15) + (60 * d)
print('O total do aluguel foi de R$ {:.2f}'.format(p))