p = dict()
gol = []
p["nome"] = str(input('Nome do Jogador: '))
p["partidas"] = int(input(f'Quantas partidas {p["nome"]} jogou? '))
for i in range(0, p["partidas"]):
    gol.append(int(input(f'Quantos gol na partida {i}? ')))
print(f'O jogador {p["nome"]} jogou {p["partidas"]}.')
for k, v in enumerate(gol):
    print(f'Na partida {k}, fez {v} gols.')
print(f'Foi um total de {sum(gol)}')