products = ('Pao', 1, 'Leite', 200, 'Ovos', 30)
print('=-'*15)
print('SUPERMERCADO PERLAMBUCANOS')
print('=-'*15)
for pos in range(0, len(products)):
    if pos % 2 == 0:
        print(f'{products[pos]:.<30}', end='')
    else:
        print(f'R${products[pos]:>7.2f}')
print('=-'*15)
