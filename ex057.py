sexo = str(input('Digite seu sexo [M/F]: '))
while not sexo in 'MmFf':
        sexo = str(input('Sexo incorreto, por favor digite M para masculino ou F para feminino: : '))
print(f'Sexo {sexo.upper()} registrado com suceso!')
