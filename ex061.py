t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = int(0)
while c != 10:
    print(f'{t}', end=' -> ')
    t += r
    c += 1
print('FIM')