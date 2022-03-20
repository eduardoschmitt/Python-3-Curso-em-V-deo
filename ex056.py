cont = int(0)
iH = int(0)
media = int(0)
homemVelho = ''
for c in range(0,4):
    nome = str(input(f'Digite o nome da {c+1}ª pessoa: '))
    i = int(input(f'Digite a idade da {c+1}ª pessoa: '))
    sexo = str(input(f'DIGITE O SEXO DA {c+1}ª PESSOA (M/F)'))
    media += i
    if sexo in 'Ff' and i < 20:
            cont += 1
    elif sexo in 'Mm' and i > iH:
        iH = i
        homemVelho = nome
print(f'A média de idade do grupo é {media/4:.2f}')
print(f'O nome do homem mais velho é {homemVelho}. Ele possui {iH} anos')
print(f'O número de mulheres que tem menos de 20 anos é {cont}')