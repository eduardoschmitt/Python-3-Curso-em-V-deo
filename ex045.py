import random
print('PEDRA PAPEL OU TESOURA')
print('\n1 - PEDRA\n2 - PAPEL\n3 - TESOURA')
n = int(input('\nDigite aqui: '))

n1 = random.randint(1,3)

if n1 == 1:
    n2 = 'PEDRA'
if n1 == 2:
    n2 = 'PAPEL'
if n1 == 3:
    n2 = 'TESOURA'

if n == n1:
    print(f'Empate! Ambos colocaram {n2}')
if n == 1 and n1 == 2:
    print(f'O computador venceu! Eles escolheu {n2}')
if n == 2 and n1 == 1:
    print(f'Você venceu! O computador escolheu {n2}')
if n == 3 and n1 == 1:
    print(f'O computador venceu! Eles escolheu {n2}')
if n == 1 and n1 == 3:
    print(f'Você venceu! O computador escolheu {n2}')
if n == 3 and n1 == 2:
    print(f'Você venceu! O computador escolheu {n2}')
if n == 2 and n1 == 3:
    print(f'O computador venceu! Eles escolheu {n2}')