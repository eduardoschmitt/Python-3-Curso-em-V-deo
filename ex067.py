n = int(1)
while n > 0:
    c = int(1)
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n <= 0:
        break
    while c <= 10:
        print(f'{n} X {c} = {n*c}')
        c += 1
print('\nFIM')