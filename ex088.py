import random
c = 0
res = []
n = int(input('Quantos jogos você deseja sortear? '))
while c < n:
    for i in range(6):
        num = random.randint(1, 60)
        if num not in res:
            res.append(num)
    res.sort()
    print(f'{res}', end=' ')
    print()
    c += 1
    res = []