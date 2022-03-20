pessoa = dict()
lista = list()
mulher = list()
media = 0
while True:
    pessoa["nome"] = str(input('Nome: '))
    pessoa["sexo"] = str(input('Sexo: '))
    if pessoa["sexo"] in 'Ff':
        mulher.append(pessoa["nome"])
    pessoa["idade"] = int(input('Idade: '))
    lista.append(pessoa.copy())
    c = input('Deseja continuar? [S/N] ')
    if c in 'Nn':
        break
print(f'{len(lista)} pessoas cadastradas')
for k, v in enumerate(lista):
    media += lista[k]["idade"]
media = media / len(lista)
print(media)
for k, v in enumerate(lista):
    if lista[k]["idade"] > media:
        print(f'{lista[k]} esta acima de média de idade')
print(f'as mulheres são: {mulher}')