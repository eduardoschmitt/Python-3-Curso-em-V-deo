c = 's'
total = mil = cheapPrice = int(0)
cheapName = ''
while c in 'Ss':
    productName = str(input('Nome do produto: '))
    price = float(input('Preço: R$'))
    c = str(input('Deseja continuar? [S/N] '))
    while not c in 'SsNn':
        c = str(input('Deseja continuar? [S/N] '))
    total += price
    if price > 1000:
        mil += 1
    if cheapPrice == 0:
        cheapName = productName
        cheapPrice = price
    elif price < cheapPrice:
        cheapName = productName
        cheapPrice = price
print(f'Total: R${total:.2f}')
print(f'{mil} produtos custaram mais de R$1000.00')
print(f'{cheapName} foi o produto mais barato custando R${cheapPrice:.2f}')