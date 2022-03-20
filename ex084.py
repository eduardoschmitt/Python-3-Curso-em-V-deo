np = []
lt = []
c = 'Ss'
leveNome = []
pesadoNome = []
pessoasCadastradas = 0
maisLeve = maisPesado = 0
while c in 'Ss':
    name = str(input('Digite seu nome: '))
    peso = float(input('Digite seu peso: '))
    lt.append(name)
    lt.append(peso)
    np.append(lt)
    if peso < maisLeve:
        leveNome.clear()
        maisLeve = peso
        leveNome.append(name)
    elif peso == maisLeve:
        leveNome.append(name)
    if peso > maisPesado:
        pesadoNome.clear()
        maisPesado = peso
        pesadoNome.append(name)
    elif peso == maisPesado:
        pesadoNome.append(name)
    if maisLeve == 0:
        maisLeve = peso
        leveNome.append(name)
    pessoasCadastradas += 1
    c = str(input('Deseja continuar? [S/N]'))
print(f'Você cadastrou {pessoasCadastradas} pessoas')
print(f'O maior peso foi {maisPesado:.1f}Kg. Peso de {pesadoNome}')
print(f'O menor peso foi {maisLeve:.1f}Kg. Peso de {leveNome}')
