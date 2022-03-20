matriz = [[0,0,0], [0,0,0], [0,0,0]]
for c in range(3):
    for i in range(3):
        matriz[c][i] = int(input(f'Digite o número [{c}] [{i}] da matriz: '))
for c in range(3):
    for i in range(3):
        print(f'[{matriz[c][i]}]', end=' ')
    print()