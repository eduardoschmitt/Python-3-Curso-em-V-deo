n = input('Digite um número de 0 a 9999: ')
n = n + "0000"
print(f'Unidade: {n[0]}')
print(f'Dezena: {n[1]}')
print(f'Centena: {n[2]}')
print(f'Milhar: {n[3]}')

n = int(input('Informe um número: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')