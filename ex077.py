words = ('free', 'money', 'here')
for n in words:
    print(f'{n}', end='')
    if 'a' in n:
        print(' a', end='')
    if 'e' in n:
        print(' e', end='')
    if 'i' in n:
        print(' i', end='')
    if 'o' in n:
        print(' o', end='')
    if 'u' in n:
        print(' u', end='')
    print('')

# OUTRA FORMA

for i in words:
    print(f'\nNa palavra {i.upper()} temos ', end='')
    for l in i:
        print(l)
        if l.lower() in 'aeiou':
            print(l, end=' ')