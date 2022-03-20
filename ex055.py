pesoMaior = int(0)
pesoMenor = int(1000000)

for c in range(0,5):
    peso = float(input(f'Digite o {c+1}º peso: '))
    if peso > pesoMaior:
        pesoMaior = peso
    if peso < pesoMenor:
        pesoMenor = peso
print(f'O peso maior foi {pesoMaior}')
print(f'O peso menor foi {pesoMenor}')