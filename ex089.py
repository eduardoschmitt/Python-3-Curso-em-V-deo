ficha = []
while True:
    name = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    m = (nota1+nota2)/2
    c = input('Deseja continuar? [S/N] ')
    ficha.append([name, [nota1, nota2], m])
    if c in 'Nn':
        break
for i, a in enumerate(ficha):
    print(f'{i} {a[0]} {[a[2]]}')
while True:
    opc = int(input('Mostrar as notas de qual aluno?'))
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')