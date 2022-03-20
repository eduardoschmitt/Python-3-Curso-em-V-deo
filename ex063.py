i = int(input('Digite os termos: '))
n = int(1)
na = int(0)
nb = int(0)
c = int(0)
if i == 1:
    print('0')
while c < i-1:
    nb = n
    n = na + n
    if c == 0:
        print('0', end=' -> ')
    print(f'{nb}',end=' -> ')
    na = nb
    c += 1
print('FIM')