import random
winCount = perdeu = int(0)
while perdeu == 0:
    pi = bool(input('Escolha True para par ou False para ímpar: '))
    n = int(input('Digite um número para jogar par ou ímpar: '))
    nc = random.randint(0, 10)
    print(f'Computador: Eu joguei {nc}')
    if (n + nc) % 2 == 0 and pi == True:
        print('Você ganhou')
        winCount += 1
    elif (n + nc) % 2 != 0 and pi == False:
        print('Você ganhou')
        winCount += 1
    else:
        perdeu += 1
print('Voce perdeu otario')
print(f'Sua sequencia foi de {winCount}')
