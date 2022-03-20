jogadores = list()
while True:
    p = dict()
    gol = []
    p["nome"] = str(input('Nome do Jogador: '))
    p["partidas"] = int(input(f'Quantas partidas {p["nome"]} jogou? '))
    for i in range(0, p["partidas"]):
        gol.append(int(input(f'Quantos gol na partida {i}? ')))
    p["gols"] = gol
    print(f'O jogador {p["nome"]} jogou {p["partidas"]}.')
    for k, v in enumerate(gol):
        print(f'Na partida {k}, fez {v} gols.')
    print(f'Foi um total de {sum(gol)}')
    p["total"] = sum(gol)
    print(p)
    jogadores.append(p.copy())
    cont = input('Desejar continuar? [S/N] ')
    if cont in 'Nn':
        break
print(jogadores)
for z, y in enumerate(jogadores):
    print(z, end=' ')
    print(y["nome"], end=' ')
    print(y["gols"], end=' ')
    print(y["total"], end=' ')
    print()