t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = int(0)
nt = int(10)
contador = int(0)
while nt > 0:
    while c < nt:
        print(f'{t}', end=' -> ')
        t += r
        c += 1
        contador += 1
    print('PAUSA')
    nt = int(input('\nDeseja ver mais quantos termos? '))
    c = int(0)
print(f'Processo finalizado! {contador} termos mostrados')