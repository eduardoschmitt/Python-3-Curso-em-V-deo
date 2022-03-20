c = 's'
maior = homem = mulher20 = int(0)
while c in 'Ss':
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] '))
    while not sexo in 'MmFf':
        sexo = str(input('Sexo: [M/F] '))
    c = str(input('Deseja continuar? [S/N] '))
    while not c in 'SsNn':
        c = str(input('Deseja continuar? [S/N] '))
    if idade > 18:
        maior += 1
    if sexo in 'Mm':
        homem += 1
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
print(f'{maior} pessoas tem mais de 18 anos')
print(f'{homem} homens foram cadastrados')
print(f'{mulher20} mulheres tem menos de 20 anos')