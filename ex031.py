d = int(input('Qual a distância da sua viagem em KM? '))
if d <= 200:
    print(f'O preço da viagem é de R$ {d*0.5:.2f}')
else:
    print(f'O preço da viagem é de R$ {d*0.45:.2f}')