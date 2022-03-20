import random
t = int(0)
n = int(-1)
cn = random.randint(0, 10)

while n != cn:
    n = int(input('Digite um número entre 0 e 10: '))
    t += 1
    if cn == n:
        print(f'Você acertou, o número era {cn}. Você precisou de {t} tentativas')