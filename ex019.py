import random
n1 = input('Escreva o nome do primeiro aluno')
n2 = input('Escreva o nome do segundo aluno')
n3 = input('Escreva o nome do terceiro aluno')
n4 = input('Escreva o nome do quarto aluno')
sort = random.randint(1,4)
if sort == 1:
    print(f'O escolhido foi {n1}')
if sort == 2:
    print(f'O escolhido foi {n2}')
if sort == 3:
    print(f'O escolhido foi {n3}')
if sort == 4:
    print(f'O escolhido foi {n4}')

n1 = input('Escreva o nome do primeiro aluno')
n2 = input('Escreva o nome do segundo aluno')
n3 = input('Escreva o nome do terceiro aluno')
n4 = input('Escreva o nome do quarto aluno')
lista = [n1,n2,n3,n4]
e = random.choice(lista)
print(f'O aluno escolhido foi {e}')