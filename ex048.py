s = int(0)
for c in range(3, 501, 3):
    print(c)
    if c % 2 == 0:
        s += 0
    else:
        s += c
print(f'A soma de todos os números ímpares que são múltiplos de 3 é {s}')