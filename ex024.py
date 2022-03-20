c = input('Digite o nome da sua cidade').strip()
c = c.split()
print('SANTO' in c[0].upper())

c = input('Digite o nome da sua cidade').strip()
print(c[:5].upper() == 'SANTO')