s = float(input('Digite o seu salário: '))
if s > 1250:
    s = s + (s*0.1)
else:
    s = s + (s*0.15)
print(f'O seu salário atual é de {s}')