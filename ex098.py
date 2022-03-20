def contador(i, f, p):
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if f < i and p > 0:
        p *= -1
        f -= 2
    for i in range(i, f+1, p):
        print(i, end=' ')
    print()


contador(1, 10, 1)
contador(10, 0, 2)
i = int(input('INICIO: '))
f = int(input('FIM: '))
p = int(input('PASSO: '))
contador(i, f, p)