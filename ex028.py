import random

cn = random.randint(0,5)
n = int(input('Digite um número entre 0 e 5: '))
if cn == n:
    print(f'Você acertou, o número era {cn}')
else:
    print(f'Você errou, o número era {cn}')