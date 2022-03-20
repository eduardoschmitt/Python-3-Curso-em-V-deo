v = int(input('Escreva a velocidade do carro em KM/H: '))
if v > 80:
    print('\033[31m Você foi multado!')
    m = (v - 80) * 7
    print(f'\033[33m A multa totalizou R$ {m:.2f}')
else:
    print('\033[32m Você respeitou o limite! :)')