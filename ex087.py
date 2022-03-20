matriz = [[0,0,0], [0,0,0], [0,0,0]]
somaPar = somaTres = maiorValor = 0
for c in range(3):
    for i in range(3):
        matriz[c][i] = int(input(f'Digite o número [{c}] [{i}] da matriz: '))
        if matriz[c][i] % 2 == 0:
            somaPar += matriz[c][i]
        if i == 2:
            somaTres += matriz[c][i]
        if matriz[c][i] > maiorValor:
            maiorValor = matriz[c][i]
for c in range(3):
    for i in range(3):
        print(f'[{matriz[c][i]}]', end=' ')
    print()
print(f'A soma dos valores pares é {somaPar}')
print(f'A soma dos valores da terceira coluna é {somaTres}')
print(f'O maior valor da segunda linha é {maiorValor}')