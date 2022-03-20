e = input('Digite uma expressão: ')
p = []
for c in e:
    if c == '(':
        p.append('(')
    elif c == ')':
        if len(p) > 0:
            p.pop()
        else:
            p.append(')')
            break
if len(p) == 0:
    print('Válida')
else:
    print('Inválida')