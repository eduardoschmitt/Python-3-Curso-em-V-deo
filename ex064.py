n = c = soma = int(0)
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        soma += n
        c += 1
print(f'Foram digitados {c} números. E sua soma resulta em {soma}')