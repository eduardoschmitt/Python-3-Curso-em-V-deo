action = int(4)
while action != 5:
    action = int(4)
    while action == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
        print('')
        print(20*'=-')
        print('''        [1] SOMAR 
        [2] MULTIPLICAR 
        [3] MAIOR 
        [4] NOVOS NÚMEROS 
        [5] SAIR DO PROGRAMA''')
        print(20*'=-')
        print('')
        action = int(input('Digite a operação desejada: '))

        if action == 1:
            print(f'{n1} + {n2} = {n1+n2}\n')

        elif action == 2:
            print(f'{n1} * {n2} = {n1*n2}\n')

        elif action == 3:
            if n1 > n2:
                print(f'{n1} > {n2}\n')
            if n2 > n1:
                print(f'{n2} > {n1}\n')
            if n1 == n2:
                print(f'{n2} = {n1}\n')

        else:
            if action != 4 and action !=5:
                print('Opção Invalida! Tente Novamente!\n')
print('\nFIM')