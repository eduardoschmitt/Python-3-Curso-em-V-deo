t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
for c in range(1,11):
    calc = t + (c - 1) * r
    print(calc)

for c in range(t, t + (11 - 1) * r, r):
    print(c)