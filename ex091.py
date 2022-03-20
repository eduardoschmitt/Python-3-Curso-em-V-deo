from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6),}
ranking = dict()
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print(ranking)
for i, s in enumerate(ranking):
    print(f'{i+1}ª lugar: {s[0]} com {s[1]}.')